from django.contrib import admin

from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title_en', 'title_uz', 'title_ru', 'image_uz',
                    'english', 'russian', 'uzbek', 'date', 'views']

    list_editable = ['english', 'russian', 'uzbek', 'views']

    fields = ['title_uz', 'description_uz', 'image_uz',
              ('file_uz_one', 'file_uz_two', 'file_uz_three', 'file_uz_four', 'file_uz_five', 'file_uz_six',
               'file_uz_seven', 'file_uz_eight', 'file_uz_nine', 'file_uz_ten'), 'video_title_uz', 'video_uz',
              'title_en', 'description_en', 'image',
              ('file_en_one', 'file_en_two', 'file_en_three', 'file_en_four', 'file_en_five', 'file_en_six',
               'file_en_seven', 'file_en_eight', 'file_en_nine', 'file_en_ten'), 'video_title', 'video',
              'title_ru', 'description_ru', 'image_ru',
              ('file_ru_one', 'file_ru_two', 'file_ru_three', 'file_ru_four', 'file_ru_five', 'file_ru_six',
               'file_ru_seven', 'file_ru_eight', 'file_ru_nine', 'file_ru_ten'), 'video_title_ru', 'video_ru',
              'date', 'extra_img_one', 'extra_img_two', 'extra_img_three',
              'english', 'russian', 'uzbek']

    search_fields = ['title_en', 'title_uz', 'title_ru']


admin.site.site_header = "Joint Project Implementation Unit"
admin.site.register(News, NewsAdmin)
