from django.urls import path
from django.views.generic import TemplateView
from frontend import views

urlpatterns=[
path("",views.reactpy("frontend.pages.home.HomePage"),name="home"),
path("login/",TemplateView.as_view(template_name="frontend/login.html")),
path("dashboard/user/",views.reactpy("frontend.pages.user_dashboard.UserDashboardPage")),
path("dashboard/beneficiary/",views.reactpy("frontend.pages.beneficiary_dasboard.BeneficiaryDashboardPage")),
path("dashboard/guardian/",views.reactpy("frontend.pages.guardian_dashboard.GuardianDashboardPage")),
path("packages/",views.reactpy("frontend.pages.milestone.MilestonesPage")),
path("package/create/",views.reactpy("frontend.pages.package.PackagePage")),
path("package/<int:pack_id>/",views.reactpy("frontend.pages.package_card.PackageCard")),
path("milestone/",views.reactpy("frontend.pages.milestone.MilestonesPage")),
path("milestone/create/",views.reactpy("frontend.pages.milestone_create.CreateMilestonePage")),
path("milestone/upload/",views.reactpy("frontend.pages.milestone_upload.UploadMilestonePage")),
path("milestone/preview/",views.reactpy("frontend.pages.milestone_preview.MilestoneDetailsPage")),
path("notification/",views.reactpy("frontend.pages.notification.NotificationPage")),
path("access-logs/",views.reactpy("frontend.pages.access_log.AccessLogsPage")),
path("explorer/",views.reactpy("frontend.pages.package_explorer.PackageExplorerPage")),
path("switch-role/",views.reactpy("frontend.pages.switch_role.SwitchRolePage")),
path("account/settings/",views.reactpy("frontend.pages.account.settings.AccountsettingsPage")),
path("account/settings/email/",views.reactpy("frontend.pages.account.change_email.ChageEmailPage")),
path("account/setings/password/",views.reactpy("frontend.pages.account.change_password.ChangePasswordPage")),
path("account/settings/security-log/",views.reactpy("frontend.pages.account.security_log.SecurityLogPage")),
path("account/settings/2fa/",views.reactpy("frontend.pages.account.two_factor.TwoFactorPage")),
path("supervised/<int:package_id>/",views.reactpy("frontend.pages.guardian_review.GuardianReviewPage")),
path("request-supervision/",views.reactpy("frontend.pages.request_supervision.RequestSupervisionPage")),
path("communcation-detals/",views.reactpy("frontend.pages.communcaiont_details.CommuncationDetailsPage")),
path("communcation-form/",views.reactpy("frontend.pages.communication_form.CommunicationFormPage")),
path("communcation-list/",views.reactpy("frontend.pages.communication_list.CommunicationListPage"))
]
