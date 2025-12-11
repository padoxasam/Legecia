from django.urls import path
from django.views.generic import TemplateView
from frontend.pages.milestone import MilestonesPage
from frontend.pages.milestone_create import CreateMilestonePage
from frontend.pages.milestone_upload import UploadMilestonePage
from frontend.pages.milestone_preview import MilestoneDetailsPage
from frontend.pages.user_dashboard import UserDashboardPage
from frontend.pages.beneficiary_dasboard import BeneficiaryDashboardPage
from frontend.pages.guardian_dashboard import GuardianDashboardPage
from . import views
from frontend.pages.package import PackagePage
from frontend.pages.package_form import PackageForm
from frontend.pages.package_card import PackageCard
from frontend.pages.notification import NotificationPage
from frontend.pages.access_log import AccessLogsPage
from frontend.pages.package_explorer import PackageExplorerPage
from frontend.pages.switch_role import SwitchRolePage
from frontend.pages.account.settings import AccountsettingsPage
from frontend.pages.account.two_factor import TwoFactorPage
from frontend.pages.account.change_email import ChageEmailPage
from frontend.pages.account.change_password import ChangePasswordPage
from frontend.pages.account.security_log import SecurityLogPage
from frontend.pages.request_supervision import RequestSupervisionPage
from frontend.pages.guardian_review import GuardianReviewPage
from frontend.pages.communcaiont_details import CommuncationDetailsPage
from frontend.pages.communication_form import CommunicationFormPage
from frontend.pages.communication_list import CommunicationListPage
#from reactpy_django.http import ReactPyView
from frontend.pages.home import HomePage
urlpatterns=[
    path('',TemplateView.as_view(template_name="frontend/home.html"),name='view'),
    path("login/", TemplateView.as_view(template_name="frontend/login.html")),
    path('dashboard/user/',views.UserDashboardPage,name='User Dashboard'),
    path('dashboard/beneficiary/',views.BeneficiaryDashboardPage,name='Beneficiary Dashboard'),
    path('dashboard/guardian/',views.GuardianDashboardPage,name='Guardian Dashboard'),
    path('packages/',views.MilestonesPage,name='Main package'),
    path('package/create/',views.PackageForm,name='Create Package'),
    path('package/<int:pack_id>/',views.PackageCard,name='Package Details'),
    path('milestone/',views.MilestonesPage,name='Milestone'),
    path('milestone/create/',views.CreateMilestonePage,name='Milestone Create'),
    path('milestone/upload/',views.UploadMilestonePage,name='Milestone upload'),
    path('milestone/preview/',views.MilestoneDetailsPage,name='Milestone preview'),
    path('notification/',views.NotificationPage),
    path("access-logs/", views.AccessLogsPage, name="access_logs"),
    path('explorer/' ,views.PackageExplorerPage),
    path('switch-role/', views.SwitchRolePage, name='switch_role'),
    path('account/settings/',views.AccountsettingsPage),
    path('account/settings/email/',views.ChageEmailPage),
    path('account/setings/password/',views.ChangePasswordPage),
    path('account/settings/security-log/',views.SecurityLogPage),
    path('account/settings/2fa/',views.TwoFactorPage),
    path('supervised/<int:package_id>/', views.GuardianReviewPage),
    path('request-supervision/',views.RequestSupervisionPage),
    path('communcation-detals/')

    ]
    
