# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
import time
from openerp.osv import fields, osv

class sale_order(osv.osv):
    _inherit = 'sale.order'
    _columns = {
        'sale_roster_line': fields.one2many('driver.roster.line','sale_order_id',string="Sale Roster Lines")
    }

#get sale orders in the selected roster date and order state in progress/manual only
    def _search(self, cr, user, args, offset=0, limit=None, order=None, context=None, count=False, access_rights_uid=None):
        if context is None:
            context={}
        so_ids=[]
        if context.get('roster') and not context.get('roster_date'):
            args.append(['id', 'in', so_ids])
        if context.get('roster') and context.get('roster_date'):
            date = context.get('roster_date')
            qry = """select id from sale_order where state in ('progress','manual') and date_order >= '%s' and date_order < ('%s'::date + '1 day'::interval)"""%(date,date)
            cr.execute(qry)
            res = cr.fetchall()
            if res:
                so_ids.extend([i[0] for i in res])
            args.append(['id', 'in', so_ids])
        return super(sale_order, self)._search(cr, user, args, offset=offset, limit=limit, order=order, context=context)

