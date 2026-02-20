from odoo import models, fields

class TipoPropiedadesInmobiliarias(models.Model):
    _name = 'tipo.propiedades.inmobiliarias'
    _description = 'Tipo de propiedades inmobiliarias'

    name = fields.Char(required=True)
    descripcion = fields.Text()
