from odoo import models, fields, api

# Création de modèle Voyage pour stocker les informations sur les voyages.
class Voyage(models.Model):
    _name = 'contact_travel.voyage'
    _description = 'Modél pour stocker les informations sur les voyages'

    name = fields.Char(string='Voyage') # Champ pour le nom du voyage
    departure_date = fields.Date(string='Date de Départ')  # Champ pour la date de départ
    destination = fields.Char(string='Distination') # Champ pour la destination
    contact_id = fields.Many2one('res.partner', string='Contact') # Champ pour lier le contact associé
    amount = fields.Float(string='Montant du Voyage') # Champ pour le montant du voyage 

   
   #Héritage du modèle 'res.partner' pour gérer les voyages associés aux contacts
class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    # Relation inverse pour lier les voyages aux contacts
    voyage_ids = fields.One2many('contact_travel.voyage', 'contact_id', string='Voyages') 
    # Champ pour calculer le nombre de voyages
    nmbr_voyages = fields.Integer(string='Nombre de Voyages', compute='_compute_voyages_number') 

    # Fonction pour ouvrir la fenêtre des voyages 
    # associés au contact
    def action_open_voyages(self):          

        domain = [('contact_id', 'in', self.ids)]
        action = {
            'name': 'Voyages de l\'Utilisateur',
            'type': 'ir.actions.act_window',
            'res_model': 'contact_travel.voyage',
            'view_mode': 'tree,form',
            'domain': domain,
        }

        return action


    
    @api.depends('voyage_ids')
    # Fonction pour calculer le nombre de voyages 
    # associés au contact
    def _compute_voyages_number(self):
        for rec in self:
            rec.nmbr_voyages = len(rec.voyage_ids)

    # Champ pour le Niveau de récompense, 
    # de type séléction (Argent, Or, Platine)
    reward_level = fields.Selection(
        [('argent', 'Argent'), ('or', 'Or'), ('platine', 'Platine')],
        string='Niveau de Récompense',
        default='argent',
        compute='_compute_reward_level' 
    )

    @api.depends('voyage_ids.amount')
    # Fonction automatique pour 
    # le calcul du niveau de récompense 
    # en fonction du montant total des voyages
    def _compute_reward_level(self): 
        for rec in self:
            total_amount = sum(rec.voyage_ids.mapped('amount'))
        if total_amount >= 100000:
            rec.reward_level = 'platine'
        elif total_amount >= 50000:
            rec.reward_level = 'or'
        else:
            rec.reward_level = 'argent'



 
 
            