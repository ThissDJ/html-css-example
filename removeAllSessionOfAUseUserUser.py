
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
import datetime
def all_unexpired_sessions_for_user(user):
    user_sessions = []
    all_sessions  = Session.objects.filter(expire_date__gte=datetime.datetime.now())
    for session in all_sessions:
        session_data = session.get_decoded()
        if user.pk == session_data.get('_auth_user_id'):
            user_sessions.append(session.pk)
    return Session.objects.filter(pk__in=user_sessions)

def delete_all_unexpired_sessions_for_user(user, session_to_omit=None):
    session_list = all_unexpired_sessions_for_user(user)
    if session_to_omit is not None:
        session_list.exclude(session_key=session_to_omit.session_key)
    session_list.delete()

user = User.objects.get(username= 'weberchen1')
delete_all_unexpired_sessions_for_user(user)
