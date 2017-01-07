from studentsdb.settings import BASE_URL


def students_processor(request):
    return {'BASE_URL': BASE_URL}
