from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import (
    CreateView,
    TemplateView,
    DetailView,
)
from talks.models import (Talk_Type, Proposal)
from talks.forms import ProposalForm
from .mixins import LoginRequiredMixin

class CreateTalk(LoginRequiredMixin, CreateView):
    model = Proposal
    form_class = ProposalForm
    template_name = "talks/talk_form.html"


    def get_form_kwargs(self):
        kwargs = super(CreateTalk, self).get_form_kwargs()
        return kwargs

    def get_contex_data(self, **kwargs):
        context = super(CreateTalk, self).get_context_data(**kwargs)
        return context
    
    def get_form_valid_message(self):
        msg = ugettext('Talk proposal <strong>{title}</strong> created.')
        return format_html(msg, title=self.object.title)
    

    def form_valid(self, form):

        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        
        # Save the author information as well (many-to-many fun)
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())

class TalkView(DetailView):
    model = Proposal
    template_name = "talks/talk.html"

    def get_object(self,*args, **kwargs):
        object = super(TalkView, self).get_object(*args, **kwargs)
        return object

    def get_contex_data(self, **kwargs):
        context = super(TalkView, self).get_contex_data(**kwargs)
        return context

