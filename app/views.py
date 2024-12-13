from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets,status
from .serializers import LinkSerializer
from .models import Link


class PostBucket(APIView):
    def post(self,request):
        title = request.data.get("title")
        content = request.data.get("content")
        link_serializer = LinkSerializer(data=request.data)
        if link_serializer.is_valid():
            link_serializer.save(title=title,content=content)
            return Response(link_serializer.data, status=status.HTTP_201_CREATED)
        return Response(link_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


class GetBucket(APIView):
    def get(self,request,url_id):
        # query = request.query_params.get("72FDc5C2")
        # query2 = "72FDc5C2"
       
        try:
            bucket = Link.objects.get(url_id=url_id).url_id
        except Link.DoesNotExist:
            return Response({'error': 'Link not found'}, status=status.HTTP_404_NOT_FOUND)       
        
        link = LinkSerializer(Link.objects.get(url_id=bucket)).data
        return Response(link,status=status.HTTP_200_OK)
        
        
