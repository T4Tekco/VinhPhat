# -*- coding: utf-8 -*-
# from odoo import http


# class Chamcong(http.Controller):
#     @http.route('/chamcong/chamcong', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/chamcong/chamcong/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('chamcong.listing', {
#             'root': '/chamcong/chamcong',
#             'objects': http.request.env['chamcong.chamcong'].search([]),
#         })

#     @http.route('/chamcong/chamcong/objects/<model("chamcong.chamcong"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('chamcong.object', {
#             'object': obj
#         })
