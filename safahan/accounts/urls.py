
from .views import AlarmDetailUpdateDeleteView, AlarmListCreateView, CoinScoutDetailUpdateDeleteView, ConditionsDetailUpdateDeleteView, ConditionsListCreateView, FilterListCreateView, FilterRetrieveUpdateDelete, GetCodeForVerify, PermiumAccountListCreateView, PermiumAccountRetrieveUpdateDelete, RankListCreateView, RankRetrieveUpdateDelete, StockScoutDetailUpdateDeleteView, VerifyPhoneNumber
from django.urls import path





urlpatterns = [
    
    path("permium-account/",PermiumAccountListCreateView.as_view(),name="all-permium-ac"),
    path("permium-account/me/",PermiumAccountRetrieveUpdateDelete.as_view(), name='permium'),
    path("filter/", FilterListCreateView.as_view(), name="all-filter"),
    path('filter/me', FilterRetrieveUpdateDelete.as_view(), name="filter"),
    path('condition/', ConditionsListCreateView.as_view(), name="conditions"),
    path('conditions/<int:id>/', ConditionsDetailUpdateDeleteView.as_view(), name='condition'),
    path('rank/', RankListCreateView.as_view(), name='rank'),
    path('rank/<int:id>/', RankRetrieveUpdateDelete.as_view(), name='rank'),
    path('verify-phone-number/', VerifyPhoneNumber.as_view(), name='verify-phone-number'),
    path('get-code-for-verify/', GetCodeForVerify.as_view(), name='get-code-for-verify'),
    path('alarm/', AlarmListCreateView.as_view(), name='alarm'),
    path('alarm/<int:pk>', AlarmDetailUpdateDeleteView.as_view(), name='alarm-detail'),
    path('stock-scout/', StockScoutDetailUpdateDeleteView.as_view(), name='stock'),
    path('coin/', CoinScoutDetailUpdateDeleteView.as_view(), name='coin')
    
    
    
    
    
    


]