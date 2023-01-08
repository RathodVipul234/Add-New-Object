from django.db.models import CASCADE
from django.contrib.admin.widgets import RelatedFieldWidgetWrapper
from django.urls import reverse

class RelatedFieldWidgetWrapper1(RelatedFieldWidgetWrapper):
    template_name = 'related_widget_wrapper.html'
    # def __init__(self,form_obj,*args, **kwargs):
    def __init__(self, widget, rel, admin_site, form_obj,can_add_related=None,
                 can_change_related=False, can_delete_related=False,
                 can_view_related=False):
        self.needs_multipart_form = widget.needs_multipart_form
        self.attrs = widget.attrs
        self.choices = widget.choices
        self.widget = widget
        self.rel = rel
        self.form_obj = form_obj
        # Backwards compatible check for whether a user can add related
        # objects.
        if can_add_related is None:
            can_add_related = rel.model in admin_site._registry
        self.can_add_related = can_add_related
        # XXX: The UX does not support multiple selected values.
        multiple = getattr(widget, 'allow_multiple_selected', False)
        self.can_change_related = not multiple and can_change_related
        # XXX: The deletion UX can be confusing when dealing with cascading deletion.
        cascade = getattr(rel, 'on_delete', None) is CASCADE
        self.can_delete_related = not multiple and not cascade and can_delete_related
        self.can_view_related = not multiple and can_view_related
        # so we can check if the related object is registered with this AdminSite
        self.admin_site = admin_site

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        rel_opts = self.rel.model._meta
        model_name = rel_opts.model_name
        context["popup_id"] = model_name
        context["form_obj"] = self.form_obj
        context["submit_url"] = reverse(
            "add_new_object",
            kwargs={
                'modelname': model_name,
                'appname': self.rel.model._meta.app_label
            }
        )
        return context
