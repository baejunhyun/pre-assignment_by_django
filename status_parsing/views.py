from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from . import models
import re


def package_list_view(request):
    context = {}
    context["package"] = models.PackageModel.objects.all().order_by("name")
    return render(request, "status_parsing/package_list_view.html", context=context)


def package_detail_view(request, pk=None):
    context = {}
    tf = models.PackageModel.objects.get(pk=pk)
    depends = tf.depends.replace("[", "").replace("]", "").split(",")

    context = {
        "package": tf,
        "depends": models.PackageModel.objects.filter(name__in=depends),
        "r_depend": models.PackageModel.objects.filter(
            depends__icontains="[" + tf.name + "]"
        ).order_by("name"),
    }

    return render(request, "status_parsing/package_detail_view.html", context=context)


def package_parsing_view(request):
    models.PackageModel.objects.all().delete()
    with open("status.real.txt", "r") as f:
        # with open ("./pre-assignment_by_django/status.real.txt", "r") as f:
        pattern = "^[A-Za-z-]+:.+"
        p = re.compile(pattern)
        pack_inst = None
        desp = " "
        is_description = False
        while True:
            text = f.readline()
            if not text:
                break
            if p.match(text):
                if is_description:
                    pack_inst.description = desp
                    pack_inst.save()
                    is_description = False
                clean_text = text.strip()
                token = clean_text.split(":")
                if clean_text.startswith("Package"):
                    pack_inst = models.PackageModel()
                    pack_inst.name = token[1].strip()
                elif clean_text.startswith("Depends"):
                    depends = token[1].strip()
                    depends_each = depends.split(",")
                    depends_result = []
                    for d in depends_each:
                        d_name = d.strip().split(" ")[0].strip()
                        if d_name not in depends_result:
                            depends_result.append("[" + d_name + "]")
                    pack_inst.depends = ",".join(depends_result)
                    if len(pack_inst.depends) > 0 and pack_inst.depends[-1] == ",":
                        pack_inst.depends = pack_inst.depends[:-1]
                    pack_inst.save()
                elif clean_text.startswith("Description"):
                    is_description = True
                    desp = " "
                    desp += token[1].strip()
                else:
                    pass
            else:
                if is_description:
                    clean_text = text.strip()
                    desp += clean_text

    return HttpResponseRedirect(reverse("status_parsing:package_list_view"))
