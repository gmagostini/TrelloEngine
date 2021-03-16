from .base import Base


class Board(Base):

    def __init__(self, app_key: str, token: str,id=None):
        super(Board, self).__init__(app_key=app_key,token=token, id=id)
        self.request_url = self.request_url + "/boards"

    def get_membership(self, id: str = None, filter: str = 'all', org_member_type: bool = False, member: bool = False, member_field: str = None):
        """
        ottieni il member proprietario della board \n
        problemi: member
        :param id: id della board
        :param filter: filtro per la board valori [admins, all, none, normal]
        :param org_member_type: mostra lo status del member nel organizzaione
        :param member: deternuba se allagare l'oggeto member
        :param member_field: se member=True seleziona i field da allegare
        :return:ritorna un dizzionario contentente il mbember
        """

        member = 'true' if member else 'false'
        org_member_type = 'true' if org_member_type else 'false'

        if id == None:
            url_temp = self.request_url + f"/{self.id}/memberships"
        else:
            url_temp = self.request_url + f"/{id}/memberships"

        query = {
            'key': self.app_key,
            'token': self.token,
            'filter': filter,
            'orgMemberType': org_member_type,
            'member': member,
            'member_fields': member_field
        }

        return super(Board, self).get_request(url_temp, query)

    def get_board(self, id: str = None, actions: str = 'all', board_stars: str = None,cards: str = None, card_plugin_data: bool = False, checklists: str = None, custom_fields: bool = False,
                  fields: str = "name,desc,descData,closed,idOrganization,pinned,url,shortUrl,prefs,labelNames", labels: str = None, lists: str = 'open', members: str = None,
                  memberships: str = None, plugin_data: bool = False, organization: str = False, organization_plugin_data:bool = False, my_prefs:bool = False, tags: bool = False):
        if id == None:
            url_temp = self.request_url + f"/{self.id}"
        else:
            url_temp = self.request_url + f"/{id}"

        card_plugin_data = 'true' if card_plugin_data else 'false'
        custom_fields = 'true' if custom_fields else 'false'
        plugin_data = 'true' if plugin_data else 'false'
        organization_plugin_data = 'true' if organization_plugin_data else 'false'
        my_prefs = 'true' if my_prefs else 'false'
        tags = 'true' if tags else 'false'

        query = {
            'key': self.app_key,
            'token': self.token,
            'actions': actions,
            'boardStars': board_stars,
            'cards': cards,
            'card_pluginData': card_plugin_data,
            'checklists': checklists,
            'customFields': custom_fields,
            'fields': fields,
            'labels': labels,
            'lists': lists,
            'members': members,
            'memberships': memberships,
            'pluginData': plugin_data,
            'organization': organization,
            'organization_pluginData': organization_plugin_data,
            'myPrefs': my_prefs,
            'tags': tags
        }

        return super(Board, self).get_request(url_temp, query)

    def update_board(self, id=None, **kwargs):
        """
        aggiorna la tabella seondo i paramteri passsati in kwarg \n
        :param id:
        :param kwargs: name desc descData closed idOrganization idEnterprise pinned url shortUrl prefs labelNames
        :return: None
        """
        if id == None:
            url_temp = self.request_url + f"/{self.id}"
        else:
            url_temp = self.request_url + f"/{id}"

        query = {
            'key': self.app_key,
            'token': self.token,
            **kwargs
        }

        return super(Board, self).put_request(url_temp, query)

    def delete_board(self, id=None):
        """
        cancella la board definitivamente
        :param id: l'id della board
        :return: dizzionario vuoto se tutto va bene
        """
        if id == None:
            url_temp = self.request_url + f"/{self.id}"
        else:
            url_temp = self.request_url + f"/{id}"

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super(Board, self).delete_request(url_temp, query)

    def get_field(self, field: str, id:str = None):
        """
        richiedri specifico field
        :param field: il filed da visionare [closed, dateLastActivity, dateLastView, desc, descData, idMemberCreator,
            idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed, url]
        :return: il filed???
        """

        if id == None:
            url_temp = self.request_url + f"/{self.id}/{field}"
        else:
            url_temp = self.request_url + f"/{id}/{field}"

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super(Board, self).get_request(url_temp, query)

    def get_actions(self, id:str = None, filter: str = None):
        """
        ottieni la lista delle actions
        :param id: id  della board
        :param filter: a comma separeted list of action (https://developer.atlassian.com/cloud/trello/guides/rest-api/action-types/)
        :return:
        """

        if id == None:
            url_temp = self.request_url + f"/{self.id}/actions"
        else:
            url_temp = self.request_url + f"/{id}/actions"

        query = {
            'key': self.app_key,
            'token': self.token,
            'filter': filter
        }

        return super(Board, self).get_request(url_temp, query)

    def get_a_card(self, id_card: str, id: str = None):

        if id == None:
            url_temp = self.request_url + f"/{self.id}/cards/{id_card}"
        else:
            url_temp = self.request_url + f"/{id}/cards/{id_card}"

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super(Board, self).get_request(url_temp,query)

    def get_board_stars(self, id: str = None):

        if id == None:
            url_temp = self.request_url + f"/{self.id}/boardStars"
        else:
            url_temp = self.request_url + f"/{id}/boardStars"

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super(Board, self).get_request(url_temp, query)


    def get_checklists(self, id=None):

        if id == None:
            url_temp = self.request_url + f"/{self.id}/checklists"
        else:
            url_temp = self.request_url + f"/{id}/checklists"

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super(Board, self).get_request(url_temp, query)

    def get_cards(self, id=None):

        if id == None:
            url_temp = self.request_url + f"/{self.id}/cards"
        else:
            url_temp = self.request_url + f"/{id}/cards"

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super(Board, self).get_request(url_temp, query)

    def get_filtered_card(self):
        pass

    def get_custom_fields(self, id=None):

        if id == None:
            url_temp = self.request_url + f"/{self.id}/customFields"
        else:
            url_temp = self.request_url + f"/{id}/customFields"

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super(Board, self).get_request(url_temp, query)


    def get_labels(self, id=None):

        if id == None:
            url_temp = self.request_url + f"/{self.id}/labels"
        else:
            url_temp = self.request_url + f"/{id}/labels"

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super(Board, self).get_request(url_temp, query)

    def create_label(self):
        pass


    def get_lists(self, id=None):

        if id == None:
            url_temp = self.request_url + f"/{self.id}/lists"
        else:
            url_temp = self.request_url + f"/{id}/lists"

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super(Board, self).get_request(url_temp, query)

    def create_list(self):
        pass

    def get_filtered_card(self):
        pass

    def get_members(self):
        pass

    def invite_member(self):
        pass

    def add_member(self):
        pass

    def remove_member(self):
        pass

    def update_member_status(self):
        pass

    def update_email_position(self):
        pass

    def update_id_email_list(self):
        pass

    def update_show_list_guide_pref(self):
        pass

    def update_show_sidebar_pref(self):
        pass

    def update_show_sidebarr_activity_pref(self):
        pass

    def update_show_sidebarr_board_actions_pref(self):
        pass

    def update_show_sidebarr_member_pref(self):
        pass

    def creata_board(self, name, **kwargs):
        """
        :param kwargs: name desc descData closed idOrganization idEnterprise pinned url shortUrl prefs labelNames
        :return: None
        """
        url_temp = self.request_url

        query = {
            'key': self.app_key,
            'token': self.token,
            'name': name,
            **kwargs
        }

        return super(Board, self).post_request(url_temp, query)

    def create_calender_key(self):
        pass

    def create_email_key(self):
        pass

    def create_tag(self):
        pass

    def mark_board_as_viewed(self):
        pass

    def enable_power_up(self):
        pass

    def disable_power_up(self):
        pass

    def get_enable_power_ups(self):
        pass

    def enable_a_power_up(self):
        pass

    def disable_a_power_up(self):
        pass

    def get_power_ups(self):
        pass


