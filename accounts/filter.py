from dateutil.relativedelta import relativedelta
from django.utils import timezone
from django.contrib import admin

class UserDateJoinedFilter(admin.SimpleListFilter):
    title = '유저가입일'
    parameter_name = 'date_joined_match'

    def lookups(self, request, model_admin):
        candidate = []
        start_date = timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)

        for i in range(6):
            value = '{}-{}'.format(start_date.year, start_date.month)
            label = '{}년 {}월 가입자'.format(start_date.year, start_date.month)
            candidate.append([value, label])
            start_date -= relativedelta(months=1)
        return candidate

    def queryset(self, request, queryset):
        value = self.value()

        if not value:
            return queryset
        try:
            year, month = map(int, value.split('-'))
            queryset = queryset.filter(date_joined__year=year, date_joined__month=month)
        except ValueError:
            return queryset.none()
        return queryset
