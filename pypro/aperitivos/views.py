from django.shortcuts import render


def video(request, slug):
    video = {'titulo': 'Vídeo Aperitivo: Motivação', 'vimeo_id': 498736189}
    return render(request, 'aperitivos/video.html', context={'video': video})
