from django.shortcuts import render


def page_detail_view(request, page_name):
    return render(request, 'pages/page_detail.html', {
            'page_name': page_name
            })
