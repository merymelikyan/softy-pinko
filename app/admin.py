from django.contrib import admin


from .models import (
    HeaderText, 
    FooterText, 
    TreeBlocks, 
    LeftBlock, 
    RightBlock,
    WorkProcess,
    Reviews,
    PricingPlan,
    Counter,
    Blog
)

from .admin_hooks import (
    HeaderTextAdmin, 
    FooterTextAdmin, 
    TreeBlocksAdmin, 
    LeftBlockAdmin, 
    RightBlockAdmin
    )

admin.site.register(HeaderText, HeaderTextAdmin)
admin.site.register(FooterText, FooterTextAdmin)
admin.site.register(TreeBlocks, TreeBlocksAdmin)
admin.site.register(LeftBlock, LeftBlockAdmin)
admin.site.register(RightBlock, RightBlockAdmin)
admin.site.register(WorkProcess)
admin.site.register(Reviews)
admin.site.register(PricingPlan) 
admin.site.register(Counter)
admin.site.register(Blog)