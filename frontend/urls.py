from django.urls import path
from django.views.generic import TemplateView
from frontend.pages.milestone import MilestonesPage
from frontend.pages.milestone_create import CreateMilestonePage
from frontend.pages.milestone_upload import UploadMilestonePage
from frontend.pages.milestone_preview import MilestoneDetailsPage
from frontend.pages.user_dashboard import UserDashboardPage
from frontend.pages.beneficiary_dasboard import BeneficiaryDashboardPage
from frontend.pages.guardian_dashboard import GuardianDashboardPage
from reactpy_django.http import ReactPyView
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

#from reactpy_django.http import ReactPyView
from frontend.pages.home import HomePage
urlpatterns=[
    path('',TemplateView.as_view(template_name="frontend/home.html"),name='view'),
    path("login/", TemplateView.as_view(template_name="frontend/login.html")),
    path('dashboard/user/',ReactPyView.as_view(UserDashboardPage),name='User Dashboard'),
    path('dashboard/beneficiary/',ReactPyView.as_view(BeneficiaryDashboardPage),name='Beneficiary Dashboard'),
    path('dashboard/guardian/',ReactPyView.as_view(GuardianDashboardPage),name='Guardian Dashboard'),
    path('packages/',ReactPyView.as_view(MilestonesPage),name='Main package'),
    path('package/create/',ReactPyView.as_view(PackageForm),name='Create Package'),
    path('package/<int:pack_id>/',ReactPyView.as_view(PackageCard),name='Package Details'),
    path('milestone/',ReactPyView.as_view(MilestonesPage),name='Milestone'),
    path('milestone/create/',ReactPyView.as_view(CreateMilestonePage),name='Milestone Create'),
    path('milestone/upload/',ReactPyView.as_view(UploadMilestonePage),name='Milestone upload'),
    path('milestone/preview/',ReactPyView.as_view(MilestoneDetailsPage),name='Milestone preview'),
    path('notification/',ReactPyView.as_view(NotificationPage)),
    path("access-logs/", ReactPyView.as_view(AccessLogsPage), name="access_logs"),
    path('explorer/' ,ReactPyView.as_view(PackageExplorerPage)),
    path('switch-role/', ReactPyView.as_view(SwitchRolePage), name='switch_role'),
    path('account/settings/',ReactPyView.as_view(AccountsettingsPage)),
    path('account/settings/email/',ReactPyView.as_view(ChageEmailPage)),
    path('account/setings/password/',ReactPyView.as_view(ChangePasswordPage)),
    path('account/settings/security-log/',ReactPyView.as_view(SecurityLogPage)),
    path('account/settings/2fa/',ReactPyView.as_view(TwoFactorPage)),
    path('supervised/<int:package_id>/', ReactPyView.as_view(GuardianReviewPage),),
    path('request-supervision/',ReactPyView.as_view(RequestSupervisionPage)),
    
    ]
    
