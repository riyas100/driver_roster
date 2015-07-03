# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import models, fields, api, _
from openerp.exceptions import except_orm, Warning, RedirectWarning
from dateutil.relativedelta import relativedelta
import time 
from math import *
from datetime import datetime


class driver_roster(models.Model):
    _name = 'driver.roster'
    _description = "Driver Roster"
    _rec_name='employee_id'
    employee_id = fields.Many2one('hr.employee', string='Driver',required="1")
    date = fields.Date(string='Date',required="1")
    roster_line = fields.One2many('driver.roster.line', 'roster_id', string='Roster Lines')

class driver_roster_line(models.Model):
    _name = 'driver.roster.line'
    

    sale_order_id = fields.Many2one('sale.order', string='Sale Order',required="1", domain=[('sale_roster_line','=',False)],ondelete="cascade")
    date = fields.Datetime(related='sale_order_id.date_order',string='Date')
    roster_id = fields.Many2one('driver.roster',string="Roster",ondelete="cascade")


    @api.multi
    @api.one
    @api.constrains('sale_order_id')
    def _check_constriant(self):
        sale_order_id = self.sale_order_id
        order_ids = []
        used_sale_orders = self.env['driver.roster.line'].search([('sale_order_id','=',self.sale_order_id.id)])
        for order in used_sale_orders:
            order_ids.append(order)
        if len(order_ids) > 1:
            raise Warning(_("one sales order for one driver only !"))

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:



