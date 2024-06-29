from django.shortcuts import render, get_object_or_404
from django.http import  HttpResponse
from .models import (
    HeaderText, 
    FooterText, 
    TreeBlocks,
    LeftBlock,
    RightBlock,
    WorkProcessMain,
    WorkProcessChild
    )

def index(request):
    context = {
        "header_text": HeaderText.objects.all().first(),
        "footer_text": FooterText.objects.all().first(),
        "tree_blocks": TreeBlocks.objects.all(),
        "left_block": LeftBlock.objects.all().first(),
        "right_block": RightBlock.objects.all().first(),
        "work_process_header": WorkProcessMain.objects.all().first(),
        "work_process_items": WorkProcessChild.objects.all()


    }
    return render(request,"base.html", context)
