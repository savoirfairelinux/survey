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

from openerp import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.one
    def _user_input_count(self):
        self.survey_user_input_count = len(self.survey_user_input_ids)

    survey_user_input_ids = fields.One2many(
        string='Survey user inputs',
        comodel_name='survey.user_input',
        inverse_name='partner_id',
    )

    survey_user_input_count = fields.Integer(
        string='# of Survey User Inputs',
        compute='_user_input_count'
    )
