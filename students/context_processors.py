
def students_processor(request):
    absolute_url = "{}://{}:{}".format(request.scheme,request.META['SERVER_NAME'], request.META['SERVER_PORT'])

    return {'ABSOLUTE_URL': absolute_url}
