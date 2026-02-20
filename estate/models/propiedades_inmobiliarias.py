from odoo import models, fields

class PropiedadesInmobiliarias(models.Model):
    _name = 'propiedades.inmobiliarias'
    _description = 'Propiedades inmobiliarias'

    name = fields.Char(required=True)
    descripcion = fields.Text()
    codigo_postal = fields.Char()
    fecha_disponibilidad = fields.Date(copy=False)
    precio_esperado = fields.Float(required=True)
    precio_venta = fields.Float(readonly = True, copy=False)
    dormitorios = fields.Integer()
    superficie_util = fields.Integer()
    fachadas = fields.Integer()
    garaje = fields.Boolean()
    jardin = fields.Boolean()
    superficie_jardin = fields.Integer()
    orientacion_jardin = fields.Selection([
        ('norte', 'Norte'),
        ('sur', 'Sur'),
        ('este', 'Este'),
        ('oeste', 'Oeste'),
    ], string="Orientación del Jardín"),
    active = fields.Boolean(default=True),
    state = fields.Selection([
        ('nueva', 'Nueva'),
        ('oferta_recibida', 'Oferta recibida'),
        ('oferta_aceptada', 'Oferta aceptada'),
        ('vendida', 'Vendida'),
        ('cancelada', 'Cancelada'),
    ], default='Nueva', string="Estado"),
    tipo_propiedad_id = fields.Many2one('tipo.propiedades.inmobiliarias', string="Tipo de Propiedad")
    comprador = fields.Many2one('tipo.propiedades.inmobiliarias', string="Comprador")  
    vendedor = fields.Many2one('tipo.propiedades.inmobiliarias', string="Vendedor")     

    

