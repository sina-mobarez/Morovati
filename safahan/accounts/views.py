

from xml.dom import ValidationErr
from django.db import IntegrityError
from django.forms import ValidationError
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
import pyotp
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, mixins
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login







from accounts.models import Alarm, CoinScout, Conditions, CustomUser, Filter, Permium, Rank, StockScout

from .serializers import AlarmSerializers, CoinScoutSerializer, ConditionsSerializer, FilterSerializer, GetCodeVerifyPhoneNumberSerializer, PermiumAccount, RankSerializer, StockScoutSeriallizer, UserModelLoginSerializer, UserModelSerializer, VerifyPhoneNumberSerializer




from ippanel import Client

# you api key that generated from panel
api_key = "bCk-lgVEMa522x0b4ErHBT9m12Wyl1v2AAQb7WVs71Y="

# create client instance
sms = Client(api_key)

def send_sms(receptor, token):
    
    bulk_id = sms.send(
        "+983000505",          # originator
        [f'98{receptor}'],    # recipients
        f'your otp code is :  {token}' # message
    )
    

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
    
    
    
    
    
    
    
    
#-----------------------------------------otp----------------------------------



class RegisterUser(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserModelSerializer

    @swagger_auto_schema(request_body=UserModelSerializer,
                         responses={400: "you have provided invalid parameters",
                                    200: UserModelSerializer})
    def post(self, request, *args, **kwargs):
        
        try:
            data = {}
            serializer = UserModelSerializer(data=request.data)
            if serializer.is_valid():
                account = serializer.save()
                account.is_active = True
                account.save()
                time_otp = pyotp.TOTP(account.key, interval=300)
                time_otp = time_otp.now()
                
                data["message"] = "user registered successfully, and otp is sent to your number"

            else:
                data = serializer.errors
                return Response(
                    {
                        'message': data,
                        
                    },
                    status= status.HTTP_400_BAD_REQUEST
                )
                
            print('========== OTP:',time_otp)
            send_sms(receptor=account.phone, token=time_otp)
            
            return Response(data, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            raise ValidationErr({"400": f'{str(e)}'})

        except KeyError as e:
            print(e)
            raise ValidationError({"400": f'Field {str(e)} missing'})



class LoginUser(APIView):
    @swagger_auto_schema(request_body=UserModelLoginSerializer,
                         responses={400: "account doesn't exist",
                                    200: UserModelSerializer})
    
    def post(self, request,*args, **kwargs):
        data = {}
        
        # serializer = UserModelLoginSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # valid_data = serializer.validated_data
              
        username = request.data['phone']
        password = request.data['password']
        try:

            Account = CustomUser.objects.get(phone=username)
        except BaseException as e:
            raise ValidationError({"400": f'{str(e)}'})

        token = AccessToken.for_user(Account)
    
        if not check_password(password, Account.password):
            raise ValidationError({"message": "Incorrect Login credentials"})
        
        if not Account.is_verified:
            raise ValidationError({"message": "First verify your phone number"})

        if Account:
            if Account.is_active:
                login(request, Account, backend='accounts.backends.OtpBackend')
                data["message"] = "user logged in"
                data["phone"] = Account.phone

                Res = {"data": data, "token": str(token)}

                return Response(Res, status=200)

            else:
                raise ValidationError({"400": f'Account not active'})

        else:
            raise ValidationError({"400": f'Account doesnt exist'})
        
        
        

class VerifyPhoneNumber(APIView):
    @swagger_auto_schema(request_body=VerifyPhoneNumberSerializer,
                         responses={400: "The provided code did not match or has expired",
                                    201: "Phone number verified successfully"})
    
    def post(self, request,*args, **kwargs): 
        phone = request.data['phone']
        otp_code = request.data['otp_code']
        try:

            Account = CustomUser.objects.get(phone=phone)
        except BaseException as e:
            raise ValidationError({"400": f'{str(e)}'})


        if Account:
            if not Account.is_verified:
                if Account.authenticate(otp_code):
                    Account.is_verified=True
                    Account.save()
                    return Response(dict(detail = "Phone number verified successfully"),status=201)
                else:
                    return Response(dict(detail='The provided code did not match or has expired'),status=400)
            else:
                return Response(dict(detail='PhoneNumber verified before'),status=400)

        else:
            raise ValidationError({"400": f'Account with this phone number doesnt exist'})
        
        
        

class GetCodeForVerify(APIView):
    @swagger_auto_schema(request_body=GetCodeVerifyPhoneNumberSerializer,
                         responses={400: "Account Verified before or doesn't exist",
                                    200: "Verification Code sent to your Number"})
    
    def post(self, request,*args, **kwargs): 
        phone = request.data['phone']
        try:

            Account = CustomUser.objects.get(phone=phone)
        except BaseException as e:
            raise ValidationError({"400": f'{str(e)}'})


        if Account:
            if not Account.is_verified:
                time_otp = pyotp.TOTP(Account.key, interval=300)
                time_otp = time_otp.now()
                
                send_sms(receptor=phone, token=time_otp)
                print('=========== otp : ', time_otp)
                
                return Response(dict(detail = "Verification Code sent to your Number"),status=200)
            else:
                return Response(dict(detail='PhoneNumber verified before'),status=400)

        else:
            raise ValidationError({"400": f'Account with this phone number doesnt exist'})
        
        
        

class AlarmListCreateView(ListCreateAPIView):
    queryset = Alarm.objects.all()
    serializer_class = AlarmSerializers
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
        
        

class AlarmDetailUpdateDeleteView(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Alarm.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = AlarmSerializers

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        if self.get_object().user == request.user:
            return self.update(request, *args, **kwargs)
        return HttpResponse("hey bro, you can not update this becuz not your's ")

    def patch(self, request, *args, **kwargs):
        if self.get_object().user == request.user:
            return self.partial_update(request, *args, **kwargs)
        return HttpResponse("hey bro, you can not patch on this becuz not your's ")
    
    def delete(self, request, *args, **kwargs):
        if self.get_object().user == request.user:
            return self.destroy(request, *args, **kwargs)
        return HttpResponse("hey bro, you can not delete this becuz not your's ")
    
    
    
    
class StockScoutDetailUpdateDeleteView(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = StockScout.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = StockScoutSeriallizer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        if self.get_object().user == request.user:
            return self.update(request, *args, **kwargs)
        return HttpResponse("hey bro, you can not update this becuz not your's ")

    def patch(self, request, *args, **kwargs):
        if self.get_object().user == request.user:
            return self.partial_update(request, *args, **kwargs)
        return HttpResponse("hey bro, you can not patch on this becuz not your's ")
    
    def delete(self, request, *args, **kwargs):
        if self.get_object().user == request.user:
            return self.destroy(request, *args, **kwargs)
        return HttpResponse("hey bro, you can not delete this becuz not your's ")
    
    
    
class CoinScoutDetailUpdateDeleteView(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = CoinScout.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CoinScoutSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        if self.get_object().user == request.user:
            return self.update(request, *args, **kwargs)
        return HttpResponse("hey bro, you can not update this becuz not your's ")

    def patch(self, request, *args, **kwargs):
        if self.get_object().user == request.user:
            return self.partial_update(request, *args, **kwargs)
        return HttpResponse("hey bro, you can not patch on this becuz not your's ")
    
    def delete(self, request, *args, **kwargs):
        if self.get_object().user == request.user:
            return self.destroy(request, *args, **kwargs)
        return HttpResponse("hey bro, you can not delete this becuz not your's ")