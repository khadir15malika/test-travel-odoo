from odoo import models, fields, api

class Voyage(models.Model):
    _name = 'contact_travel.voyage'
    _description = 'Modél pour stocker les informations sur les voyages'

    name = fields.Char(string='Voyage')
    departure_date = fields.Date(string='Date de Départ')
    destination = fields.Char(string='Distination')
    contact_id = fields.Many2one('res.partner', string='Contact')
    amount = fields.Float(string='Montant du Voyage')


class ResPartner(models.Model):
    _inherit = 'res.partner'

                                                                              # Relation inverse pour lier les voyages aux contacts
    voyage_ids = fields.One2many('contact_travel.voyage', 'contact_id', string='Voyages')
    nmbr_voyages = fields.Integer(string='Nombre de Voyages', compute='_compute_voyages_number')
    #mont_id= fields.Char('calculate_total_voyage_amount')

  
    def action_open_voyages(self):          
                                                                               # Vous devez définir la logique pour récupérer la liste des voyages associés à ce contact.
                                                                               # Cela dépendra de la structure de votre modèle `contact_travel.voyage` et de la manière dont vous reliez les contacts aux voyages.
                                                                               # Voici un exemple simplifié où nous supposons que le champ `contact_id` dans `contact_travel.voyage` stocke l'ID du contact associé.
        domain = [('contact_id', 'in', self.ids)]
        action = {
            'name': 'Voyages de l\'Utilisateur',
            'type': 'ir.actions.act_window',
            'res_model': 'contact_travel.voyage',
            'view_mode': 'tree,form',
            'domain': domain,
        }

        return action
                                                                     #Dans la méthode action_open_voyages, vous devez spécifier la logique pour récupérer les voyages associés à ce contact en fonction de votre modèle contact_travel.voyage. L'exemple ci-dessus suppose que le champ contact_id dans le modèle contact_travel.voyage est utilisé pour lier les voyages au contact. Vous devez adapter cette logique en fonction de votre modèle de données réel.

                                                                     #Assurez-vous d'importer correctement les modules api et models au début de votre fichier Python.

                                                                      #Avec cette méthode en place, le bouton "Voyages de l'Utilisateur" devrait maintenant rediriger l'utilisateur vers la liste des voyages associés à ce contact. N'oubliez pas de mettre à jour votre module Odoo après avoir apporté ces modifications.

      
    @api.depends('voyage_ids')
    def _compute_voyages_number(self):
        for rec in self:
            rec.nmbr_voyages = len(rec.voyage_ids)

    reward_level = fields.Selection(
        [('argent', 'Argent'), ('or', 'Or'), ('platine', 'Platine')],
        string='Niveau de Récompense',
        default='argent',
        compute='_compute_reward_level'
    )

    @api.depends('voyage_ids.amount')
    def _compute_reward_level(self):
        for rec in self:
            total_amount = sum(rec.voyage_ids.mapped('amount'))
        if total_amount >= 100000:
            rec.reward_level = 'platine'
        elif total_amount >= 50000:
            rec.reward_level = 'or'
        else:
            rec.reward_level = 'argent'



    #def calculate_total_voyage_amount(self):
        # Vous devez implémenter cette méthode pour calculer le montant total des voyages du client
        #total_amount = 0
        #for voyage in self.voyage_ids:
            #total_amount += voyage.amount  # Supposons que le modèle Voyage a un champ 'amount'
        #return total_amount
            