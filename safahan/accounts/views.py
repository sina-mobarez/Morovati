

from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, mixins




from accounts.models import Conditions, Filter, Permium, Rank

from .serializers import ConditionsSerializer, FilterSerializer, PermiumAccount, RankSerializer




class PermiumAccountListCreateView(ListCreateAPIView):
    queryset = Permium.objects.all()
    serializer_class = PermiumAccount
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
        
        

class PermiumAccountRetrieveUpdateDelete(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Permium.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = PermiumAccount

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object(request)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object(request)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)



    def get_object(self, request):
        """
        Returns the object the view is displaying.

        You may want to override this if you need to provide non-standard
        queryset lookups.  Eg if objects are referenced using multiple
        keyword arguments in the url conf.
        """
        queryset = self.filter_queryset(self.get_queryset())

        # Perform the lookup filtering.




        obj = get_object_or_404(queryset, user=request.user)

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj
    
    
    
    
    
class RankRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    def get_queryset(self):
        if self.request.method == 'GET':
            return Rank.objects.all()
        else:
            return Rank.objects.filter(filter=self.kwargs['id'])

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RankSerializer
        else:
            return RankSerializer
    
    

class FilterListCreateView(ListCreateAPIView):
    queryset = Filter.objects.all()
    serializer_class = Filter
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
        
        
        
        
class RankListCreateView(ListCreateAPIView):
    queryset = Rank.objects.all()
    serializer_class = RankSerializer
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
        
        
  
        
class ConditionsListCreateView(ListCreateAPIView):
    queryset = Conditions.objects.all()
    serializer_class = ConditionsSerializer
    permission_classes=[IsAuthenticated]
    
    
    
    
class ConditionsDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    def get_queryset(self):
        if self.request.method == 'GET':
            return Conditions.objects.all()
        else:
            return Conditions.objects.filter(filter=self.kwargs['id'])

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ConditionsSerializer
        else:
            return ConditionsSerializer

        
        
        
class FilterRetrieveUpdateDelete(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Filter.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = FilterSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object(request)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object(request)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)



    def get_object(self, request):
        """
        Returns the object the view is displaying.

        You may want to override this if you need to provide non-standard
        queryset lookups.  Eg if objects are referenced using multiple
        keyword arguments in the url conf.
        """
        queryset = self.filter_queryset(self.get_queryset())

        # Perform the lookup filtering.




        obj = get_object_or_404(queryset, user=request.user)

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj
    
    