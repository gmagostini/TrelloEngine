#!/usr/bin/env python3
from .base import Base


class Plugin(Base):
    
	
	def __init__(self, app_key: str, token: str, id=None, use_log = False):
		super(Plugin, self).__init__(app_key=app_key, token=token, id=id, use_log=use_log)
		self.base_url = self.base_url + "/plugins"

	def get_plugin(self, id: str = None):
		url_rquest = self.select_id(id=id, string=[])

		query = {
			'key': self.app_key,
			'token': self.token,
		}

		return super(Plugin, self).get_request(url=url_rquest, query=query)
		
	def update_plugin(self, id: str = None):
		url_rquest = self.select_id(id=id, string=[])

		query = {
			'key': self.app_key,
			'token': self.token,
		}

		return super(Plugin, self).put_request(url=url_rquest, query=query)
	
	def create_list_for_plugin(self, id: str = None):
		url_rquest = self.select_id(id=id, string=['listing'])

		query = {
			'key': self.app_key,
			'token': self.token,
		}

		return super(Plugin, self).put_request(url=url_rquest, query=query)

	def get_plugin_member_privacy_compliance(self, id: str = None):
		url_rquest = self.select_id(id=id, string=['listing'])

		query = {
			'key': self.app_key,
			'token': self.token,
		}

		return super(Plugin, self).put_request(url=url_rquest, query=query)

	def update_list_for_pligin(self, id: str = None, description: str = None, locale: str = None, 
								overviw: str = None, name: str = None):
		url_rquest = self.select_id(id=id, string=['listing'])

		query = {
			'key': self.app_key,
			'token': self.token,
			'description': description,
			'locale': locale,
			'overviw': overviw,
			'name': name
		}

		return super(Plugin, self).put_request(url=url_rquest, query=query)
