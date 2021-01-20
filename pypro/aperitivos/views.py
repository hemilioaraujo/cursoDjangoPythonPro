from django.shortcuts import render


def video(request, slug):
    videos = {
        'motivacao': {'titulo': 'Vídeo Aperitivo: Motivação', 'vimeo_id': 498736189},
        'instalacao-windows': {'titulo': '', 'vimeo_id': 498736190},
    }
    video = videos[slug]


    return render(request, 'aperitivos/video.html', context={'video': video})
