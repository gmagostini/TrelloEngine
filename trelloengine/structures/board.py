#!/usr/bin/env python3
from .base import Base


class Board(Base):

    def __init__(self, app_key: str, token: str,id=None):
        super(Board, self).__init__(app_key=app_key,token=token, id=id)
        self.base_url = self.base_url + "/boards"


    
    
    
    def get_membership(self, id: str = None, filter: str = 'all', org_member_type: bool = False, member: bool = False, member_field: str = None):
        """
        Get information about the memberships users have to the board.\n
        future: add activity as optional
        :param id: The ID of the board
        :param filter: the filter applied [admins, all, none, normal]
        :param org_member_type: Shows the type of member to the org the user is. For instance, an org admin will have a orgMemberType of admin.
        :param member: Determines whether to include a nested member object.
        :param member_field: Fields to show if member=true.
        :return: members list
        """

        url_rquest = self.select_id(id=id, string=[f"memberships"])

        query = {
            'key': self.app_key,
            'token': self.token,
            'filter': filter,
            'orgMemberType':  org_member_type,
            'member':  member,
            'member_fields': member_field
        }

        return super(Board, self).get_request(url=url_rquest,query=self.bool_to_string(query=query))

    

    def get_board(self, id: str = None, actions: str = 'all', board_stars: str = None,cards: str = None, card_plugin_data: bool = False, checklists: str = None, custom_fields: bool = False,
                  fields: str = 'all', labels: str = None, lists: str = 'open', members: str = None,
                  memberships: str = None, plugin_data: bool = False, organization: bool = False, organization_plugin_data:bool = False, my_prefs:bool = False, tags: bool = False):
        """
        Request a single board.\n
        * Read more about actions as nested resources https://developer.atlassian.com/cloud/trello/guides/rest-api/nested-resources/\n
        :param id: The ID of the board
        :param actions: Nested resource.*
        :param board_stars: [i have no idea. Documentation: string Valid values are one of: mine or none. Default: none]
        :param cards: Nested resource.*
        :param card_plugin_data: Use with the cards param to include card pluginData with the response
        :param checklists: Nested resource.*
        :param custom_fields: Nested resource.*
        :param fields: The fields of the board to be included in the response.  all or [closed, dateLastActivity,
        dateLastView, desc, descData, idMemberCreator, idOrganization, invitations, invited, labelNames,
        memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed, url]
        :param labels: Nested resource.*
        :param lists: Nested resource.*
        :param members: Nested resource.*
        :param memberships: Nested resource.*
        :param plugin_data: Determines whether the pluginData for this board should be returned.
        :param organization: Nested resource.*
        :param organization_plugin_data: Use with the organization param to include organization pluginData with the response
        :param my_prefs: i have no idea. add prefs objects maeby?
        :param tags: return the tags (aka collection) to which the board belongs
        :return: dictionary of the requested meber object
        """

        url_rquest = self.select_id(id=id)


        query = {
            'key': self.app_key,
            'token': self.token,
            'actions': actions,
            'boardStars': board_stars,
            'cards': cards,
            'card_pluginData': card_plugin_data,
            'checklists': checklists,
            'customFields':  custom_fields,
            'fields': fields,
            'labels': labels,
            'lists': lists,
            'members': members,
            'memberships': memberships,
            'pluginData':  plugin_data,
            'organization':  organization,
            'organization_pluginData':  organization_plugin_data,
            'myPrefs':  my_prefs,
            'tags':  tags
        }

        return super(Board, self).get_request(url=url_rquest,query=self.bool_to_string(query=query))

    def update_board(self, id: str = None, name: str = None, desc:str = None, closed: bool = None, subscribed: str = None,
                     id_organization: str = None, permission_level: str = None, self_join: bool = None, card_cover: bool = None,
                     hide_votes: bool = None,invitation: str = None, voting: str = None, comment: str = None, background: str = None,
                     card_aging: str = None,calender_feed_enable: bool = None, label_green: str = None, label_yellow: str = None,
                     label_orange: str = None, label_red: str = None, label_purple: str = None, label_blue: str = None):
        """
        Update board \n
        None parameter will not be change
        :param id: The ID of the board
        :param name: The new name for the board. 1 to 16384 characters long.\n
        :param desc:  A new description for the board, 0 to 16384 characters long\n
        :param closed: Whether the board is closed\n
        :param subscribed: Whether the acting user is subscribed to the board\n
        :param id_organization: The id of the team the board should be moved to\n
        :param permission_level:  permission write read. One of: org, private, public\n
        :param self_join: Whether team members can join the board themselves\n
        :param card_cover: Whether card covers should be displayed on this board\n
        :param hide_votes: Determines whether the Voting Power-Up should hide who voted on cards or not.\n
        :param invitation: Who can invite people to this board. One of: admins, members\n
        :param voting: Who can vote on this board. One of disabled, members, observers, org, public\n
        :param comment: Who can comment on cards on this board. One of: disabled, members, observers, org, public
        :param background: The id of a custom background or one of: blue, orange, green, red, purple, pink, lime, sky, grey\n
        :param card_aging: [no clue] One of: pirate, regular\n
        :param calender_feed_enable: Determines whether the calendar feed is enabled or not.\n
        :param label_green: Name for the green label. 1 to 16384 characters long\n
        :param label_yellow: Name for the yellow label. 1 to 16384 characters long\n
        :param label_orange: Name for the orange label. 1 to 16384 characters long\n
        :param label_red: Name for the red label. 1 to 16384 characters long\n
        :param label_purple:  Name for the purple label. 1 to 16384 characters long\n
        :param label_blue: Name for the blue label. 1 to 16384 characters long\n
        :return:
        """
        url_rquest = self.select_id(id=id)

        query = {
            'key': self.app_key,
            'token': self.token,
            'name': name,
            'desc': desc,
            'closed': closed,
            'subscribed': subscribed,
            'idOrganization': id_organization,
            'prefs/permissionLevel': permission_level,
            'prefs/selfJoin': self_join,
            'prefs/cardCovers': card_cover,
            'prefs/hideVotes': hide_votes,
            'prefs/invitations': invitation,
            'prefs/voting': voting,
            'prefs/comments': comment,
            'prefs/background': background,
            'prefs/cardAging': card_aging,
            'prefs/calendarFeedEnabled': calender_feed_enable,
            'labelNames/green': label_green,
            'labelNames/yellow': label_yellow,
            'labelNames/orange': label_orange,
            'labelNames/red': label_red,
            'labelNames/purple': label_purple,
            'labelNames/blue': label_blue
        }

        return super(Board, self).put_request(url=url_rquest,query=query)

    def delete_board(self, id=None):
        """
        Delete a board.\n
        :param id: The ID of the board
        :return: dizzionario vuoto se tutto va bene
        """
        url_rquest = self.select_id(id=id)

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super(Board, self).delete_request(url=url_rquest,query=query)

    def get_field(self, field: str, id:str = None):
        """
        Get a single, specific field on a board.\n
        :param field: il filed da visionare [closed, dateLastActivity, dateLastView, desc, descData, idMemberCreator,
            idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink,
            shortUrl, starred, subscribed, url]
        :param id: The ID of the board
        :return: il filed???
        """

        url_rquest = self.select_id(id=id, string=[f"{field}"])

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super(Board, self).get_request(url=url_rquest,query=query)

    def get_actions(self, id:str = None, filter: str = None):
        """
        ottieni la lista delle actions
        :param id: The ID of the board
        :param filter: a comma separeted list of action
            (https://developer.atlassian.com/cloud/trello/guides/rest-api/action-types/)
        :return:
        """

        url_rquest = self.select_id(id=id, string=[f"actions"])

        query = {
            'key': self.app_key,
            'token': self.token,
            'filter': filter
        }

        return super(Board, self).get_request(url=url_rquest,query=query)

    def get_a_card(self, id_card: str, id: str = None):
        """
        Get a single Card on a Board.\n
        :param id_card: The id the card to retrieve.
        :param id: The ID of the board
        :return: card dict
        """

        url_rquest = self.select_id(id=id, string=[f"cards",f"{id_card}"])

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super(Board, self).get_request(url_rquest,query)

    def get_board_stars(self, id: str = None):
        """
        Get all elements with star. maybe.
        :param id: The ID of the board
        :return: star list
        """

        url_rquest = self.select_id(id=id, string=[f"boardStars"])

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super(Board, self).get_request(url=url_rquest,query=query)


    def get_checklists(self, id=None):
        """
        Get all of the checklists on a Board.
        :param id: The ID of the board
        :return: checklist list
        """

        url_rquest = self.select_id(id=id, string=[f"checklists"])

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super(Board, self).get_request(url=url_rquest,query=query)

    def create_checklist(self, name: str, id: str = None):
        """
        Create a new checklist on a board.
        DOSN'T WORK
        {'response': <Response [400]>, 'text': 'invalid value for idCard'}
        I have no idea how this is supposed to work
        :param name: The name of the checklist to be created. 1 to 16384 characters long.
        :param id: The ID of the board
        :return: checklist dict
        """

        url_rquest = self.select_id(id=id, string=[f"checklists"])

        query = {
            'key': self.app_key,
            'token': self.token,
            'name': name
        }

        return super(Board, self).post_request(url=url_rquest,query=query)

    def get_cards(self, id=None):
        """
        Get all of the open Cards on a Board.
        :param id: The ID of the board
        :return: cards list
        """
        url_rquest = self.select_id(id=id, string=[f"cards"])

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super(Board, self).get_request(url=url_rquest,query=query)

    def get_filtered_card(self, filter: str, id: str = None):
        """
         Get the Cards on a Board that match a given filter.
        :param filter: the filter applied [all, closed, none, open, visible]
        :param id: The ID of the board
        :return: cards list
        """

        url_rquest = self.select_id(id=id, string=[f"cards",f"{filter}"])

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super(Board, self).get_request(url=url_rquest,query=query)

    def get_custom_fields(self, id=None):
        """
        Get the Custom Field Definitions that exist on a board.
        :param id: The ID of the board
        :return: la lista dei costumFileds
        """

        url_rquest = self.select_id(id=id, string=[f"customFields"])

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super(Board, self).get_request(url=url_rquest,query=query)


    def get_labels(self, id=None):
        """
        Get all of the Labels on a Board.
        :param id: The ID of the board
        :return: lista delle labels
        """

        url_rquest = self.select_id(id=id, string=[f"labels"])

        query = {
            'key': self.app_key,
            'token': self.token,
            'fileds': 'id,name'
        }

        return super(Board, self).get_request(url=url_rquest,query=query)

    def create_label(self, name: str, color: str, id: str = None):
        """
        create list
        :param name: nome della list
        :param color: colore
        :param id: The ID of the board
        :return: label dict
        """
        url_rquest = self.select_id(id=id, string=[f"labels"])

        query = {
            'key': self.app_key,
            'token': self.token,
            'name': name,
            'color': color
        }

        return super(Board, self).post_request(url=url_rquest,query=query)


    def get_lists(self, id: str = None):
        """
        Get the Lists on a Board
        :param id: The ID of the board
        :return: lists list
        """

        url_rquest = self.select_id(id=id, string=[f"lists"])

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super(Board, self).get_request(url=url_rquest,query=query)

    def create_list(self, name: str, id: str = None, pos: str = "top"):
        """
        Create a new List on a Board.
        :param name: nome della list
        :param color: colore
        :param id: The ID of the board
        :param pos: Determines the position of the list. Valid values: top, bottom, or a positive number.
        :return: list dict
        """

        url_rquest = self.select_id(id=id, string=[f"lists"])

        query = {
            'key': self.app_key,
            'token': self.token,
            'name': name,
            'pos': pos
        }

        return super(Board, self).post_request(url=url_rquest,query=query)


    def get_filtered_list(self, filter: str, id: str = None):
        """
        Get the List on a Board that match a given filter.
        :param filter: the filter applied [all, closed, none, open]
        :param id: The ID of the board
        :return: lists list
        """

        url_rquest = self.select_id(id=id, string=[f"lists"])

        query = {
            'key': self.app_key,
            'token': self.token,
            'filter': filter
        }

        return super(Board, self).get_request(url=url_rquest,query=query)


    def get_members(self, id: str = None):
        """
        ottieni i member apperteneti alla board
        :param id: The ID of the board
        :return: la lista dei member
        """

        url_rquest = self.select_id(id=id, string=[f"members"])

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super(Board, self).get_request(url=url_rquest,query=query)

    def invite_member(self,email:str, id: str = None, type_member: str = "normal", full_name: str = None):
        """
        Get the Members for a board
        :param email: The email address of a user to add as a member of the board.
        :param id: The ID of the board
        :param type_member: Valid values: admin, normal, observer. Determines what type of member the user being added should be of the board.
        :param full_name: The full name of the user to as a member of the board. Must have a length of at least 1 and cannot begin nor end with a space.
        :return:
        """

        url_rquest = self.select_id(id=id, string=[f"members"])

        query = {
            'key': self.app_key,
            'token': self.token,
            'email': email,
            'type': type_member,
            'fullName': full_name
        }

        return super(Board, self).put_request(url=url_rquest,query=query)

    def add_member(self,id_member: str, type_member:str, id: str = None, allow_billable_guest: bool = False):
        """
        Add a member to the board.
        :param id_member: The id of the member to add to the board.
        :param type_member: One of: admin, normal, observer. Determines the type of member this user will be on the board.
        :param id: The id of the board to update
        :param allow_billable_guest: Optional param that allows organization admins to add multi-board guests onto a board.
        :return: dict
        """
        url_rquest = self.select_id(id=id, string=[f"members",f"{id_member}"])

        query = {
            'key': self.app_key,
            'token': self.token,
            'type': type_member,
            'allowBillableGuest':  allow_billable_guest
        }
        
        return super(Board, self).put_request(url=url_rquest,query=self.bool_to_string(query=query))

    def remove_member(self,id_member: str, id: str = None) -> dict:
        """
        Remove a member to the board.
        :param id_member: The id of the member to add to the board.
        :param id: The id of the board to update
        :return: dict
        """

        url_rquest = self.select_id(id=id, string=[f"members",f"{id_member}"])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Board, self).delete_request(url=url_rquest, query=query)

    def change_membership(self, id_membership: str, type_member: str, id: str = None, member_fields: str = 'fullName, username'):
        """

        :param id_membership:
        :param type_member:
        :param id:
        :param member_fields:
        :return:
        """
        url_rquest = self.select_id(id=id, string=[f"members",f"{id_membership}"])


        query = {
            'key': self.app_key,
            'token': self.token,
            'type': type_member,
            'member_fields ': member_fields
        }

        return super(Board, self).put_request(url=url_rquest,query=query)

    def update_email_position(self, value:str, id: str = None):
        url_rquest = self.select_id(id=id, string=[f"myPrefs","emailPosition"])

        query = {
            'key': self.app_key,
            'token': self.token,
            'value': value
        }

        return super(Board, self).put_request(url=url_rquest, query=query)

    def update_id_email_list(self, value:str, id: str = None):
        url_rquest = self.select_id(id=id, string=[f"myPrefs","idEmailList"])


        query = {
            'key': self.app_key,
            'token': self.token,
            'value': value
        }

        return super(Board, self).put_request(url=url_rquest, query=query)

    def update_show_list_guide_pref(self, value:str, id: str = None):
        url_rquest = self.select_id(id=id, string=[f"myPrefs","showListGuide"])

        query = {
            'key': self.app_key,
            'token': self.token,
            'value': value
        }

        return super(Board, self).put_request(url=url_rquest, query=query)

    def update_show_sidebar_pref(self, value:str, id: str = None):
        url_rquest = self.select_id(id=id, string=[f"myPrefs","showSidebar"])

        query = {
            'key': self.app_key,
            'token': self.token,
            'value': value
        }

        return super(Board, self).put_request(url=url_rquest, query=query)

    def update_show_sidebarr_activity_pref(self, value:str, id: str = None):
        url_rquest = self.select_id(id=id, string=[f"myPrefs","showSidebarActivity"])

        query = {
            'key': self.app_key,
            'token': self.token,
            'value': value
        }

        return super(Board, self).put_request(url=url_rquest, query=query)

    def update_show_sidebarr_board_actions_pref(self, value:str, id: str = None):
        url_rquest = self.select_id(id=id, string=[f"myPrefs","showSidebarBoardActions"])

        query = {
            'key': self.app_key,
            'token': self.token,
            'value': value
        }

        return super(Board, self).put_request(url=url_rquest, query=query)

    def update_show_sidebarr_member_pref(self, value:str, id: str = None):
        url_rquest = self.select_id(id=id, string=[f"myPrefs","showSidebarMembers"])

        query = {
            'key': self.app_key,
            'token': self.token,
            'value': value
        }

        return super(Board, self).put_request(url=url_rquest, query=query)

    def create_board(self, name, default_labels: bool = True, default_lists: bool = True, desc: str = None, id_organization: str = None,
                     id_boardSource: str = None, keepFromSource: str = None, power_ups: str = None, prefs_permission_level:str = "private",
                     prefs_voting: str = "disabled", prefs_comments: str = "members", prefs_invitations: str = "members", prefs_self_join: bool = True,
                     prefs_card_covers:bool = True, prefs_background: str = "blue", prefs_card_aging: str =  "regular"):
        """
        Create a new board.
        :param name:The new name for the board. 1 to 16384 characters long.
        :param default_labels: Determines whether to use the default set of labels.
        :param default_lists: Determines whether to add the default set of lists to a board (To Do, Doing, Done). It is ignored if idBoardSource is provided.
        :param desc: A new description for the board, 0 to 16384 characters long
        :param id_organization: The id or name of the team the board should belong to.
        :param id_boardSource: The id of a board to copy into the new board.
        :param keepFromSource: To keep cards from the original board pass in the value cards
        :param power_ups: The Power-Ups that should be enabled on the new board. One of: all, calendar, cardAging, recap, voting.
        :param prefs_permission_level: The permissions level of the board. One of: org, private, public.
        :param prefs_voting: Who can vote on this board. One of disabled, members, observers, org, public.
        :param prefs_comments: Who can comment on cards on this board. One of: disabled, members, observers, org, public.
        :param prefs_invitations: Determines what types of members can invite users to join. One of: admins, members.
        :param prefs_self_join: Determines whether users can join the boards themselves or whether they have to be invited.
        :param prefs_card_covers: Determines whether card covers are enabled.
        :param prefs_background: The id of a custom background or one of: blue, orange, green, red, purple, pink, lime, sky, grey.
        :param prefs_card_aging: Determines the type of card aging that should take place on the board if card aging is enabled. One of: pirate, regular.
        :return:
        """


        url_rquest = self.base_url

        query = {
            'key': self.app_key,
            'token': self.token,
            'name': name,
            'defaultLabels':  default_labels,
            'defaultLists':  default_lists,
            'desc': desc,
            'idOrganization': id_organization,
            'idBoardSource': id_boardSource,
            'keepFromSource': keepFromSource,
            'powerUps': power_ups,
            'prefs_permissionLevel': prefs_permission_level,
            'prefs_voting': prefs_voting,
            'prefs_comments': prefs_comments,
            'prefs_invitations': prefs_invitations,
            'prefs_selfJoin':  prefs_self_join,
            'prefs_cardCovers':  prefs_card_covers,
            'prefs_background': prefs_background,
            'prefs_cardAging': prefs_card_aging

        }

        return super(Board, self).post_request(url=url_rquest,query=self.bool_to_string(query=query))

    def create_calender_key(self, id: str = None):
        """
        I don know
        :param id: The id of the board to update
        :return:
        """
        url_rquest = self.select_id(id=id, string=[f"calendarKey","generate"])

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super(Board, self).post_request(url=url_rquest, query=query)

    def create_email_key(self, id: str = None):
        """

        :param id: The id of the board to update
        :return:
        """
        url_rquest = self.select_id(id=id, string=[f"emailKey","generate"])

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super(Board, self).post_request(url=url_rquest, query=query)

    def create_tag(self, value:str, id: str = None):
        """

        :param value: The id of a tag from the organization to which this board belongs.
        :param id: The id of the board to update
        :return:
        """
        url_rquest = self.select_id(id=id, string=[f"idTags"])

        query = {
            'key': self.app_key,
            'token': self.token,
            'value': value
        }

        return super(Board, self).post_request(url=url_rquest, query=query)

    def mark_board_as_viewed(self, id: str = None):
        """
        DOSEN'T WORK !!!
        :param id: The id of the board to update
        :return:
        """
        url_rquest = self.select_id(id=id, string=[f"markedAsViewed"])

        query = {
            'key': self.app_key,
            'token': self.token
        }

        return super(Board, self).post_request(url=url_rquest, query=query)

    def enable_power_up(self, power_up:str, id: str = None):
        """

        :param value: The Power-Up to be enabled on the board. One of: calendar, cardAging, recap, voting.
        :param id: The id of the board to update
        :return:
        """
        url_rquest = self.select_id(id=id, string=[f"powerUps"])

        query = {
            'key': self.app_key,
            'token': self.token,
            'value': power_up
        }

        return super(Board, self).post_request(url=url_rquest, query=query)

    def disable_power_up(self, power_up: str, id: str = None):
        """

        :param power_up: The Power-Up to be enabled on the board. One of: calendar, cardAging, recap, voting.
        :param id: The id of the board to update
        :return:
        """
        url_rquest = self.select_id(id=id, string=[f"powerUps",f"{power_up}"])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Board, self).delete_request(url=url_rquest, query=query)

    def get_enable_power_ups(self, id: str = None):
        """
        Get the enabled Power-Ups on a board
        :param id: The id of the board to update
        :return:
        """
        url_rquest = self.select_id(id=id, string=[f"boardPlugins"])


        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Board, self).get_request(url=url_rquest, query=query)

    def enable_a_power_up(self, id_plugin: str, id: str = None):
        """
        Enable a Power-Up on a Board
        :param id: The id of the board to update
        :param idPlugin: The ID of the Power-Up to enable
        :return:
        """
        url_rquest = self.select_id(id=id, string=[f"boardPlugins"])

        query = {
            'key': self.app_key,
            'token': self.token,
            'idPlugin':id_plugin
        }

        return super(Board, self).post_request(url=url_rquest, query=query)

    def disable_a_power_up(self,id_plugin: str, id: str = None):
        """
        Disable a Power-Up on a board
        :param id: The ID of the board
        :return:
        """
        url_rquest = self.select_id(id=id, string=[f"boardPlugins",f"{id_plugin}"])

        query = {
            'key': self.app_key,
            'token': self.token,
            'idPlugin':id_plugin
        }

        return super(Board, self).delete_request(url=url_rquest, query=query)

    def get_power_ups(self, id: str = None, filter: str = None):
        """
        List the Power-Ups on a board
        :param id: The ID of the board
        :param filter: One of: enabled or available
        :return:
        """
        url_rquest = self.select_id(id=id, string=[f"plugins"])

        query = {
            'key': self.app_key,
            'token': self.token,
        }

        return super(Board, self).get_request(url=url_rquest, query=query)


