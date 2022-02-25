import os
from django.core.exceptions import ValidationError


def validate_file_extension(value):
    exten = os.path.splitext(value.name)[1]   # [0] returns path+filename
    valid_extensions = ['.pdf', '.doc', '.docx', '.xlsx', '.xls', '.txt']

    if not exten.lower() in valid_extensions:
        raise ValidationError('Неподдерживаемое расширение файла.(допустимое: .pdf, .doc, .docx, .xlsx, .xls, .txt ) ')
