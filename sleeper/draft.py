from sleeper import SleeperBase

class SleeperDraft(SleeperBase):

  def __init__(self, draft_id: str):
    super().__init__("NFL")
    draft_info = self.send_request(f"/draft/{str(draft_id)}", None)
    self.type = draft_info['data']['type']
    self.status = draft_info['data']['status']
    self.sport = draft_info['data']['sport']
    self.settings = draft_info['data']['settings']
    self.season_type = draft_info['data']['season_type']
    self.season = draft_info['data']['season']
    self.metadata = draft_info['data']['metadata']
    self.league_id = draft_info['data']['league_id']
    self.last_picked = draft_info['data']['last_picked']
    self.last_message_time = draft_info['data']['last_message_time']
    self.last_message_id = draft_info['data']['last_message_id']
    self.draft_order = draft_info['data']['draft_order']
    self.slot_to_roster_id = draft_info['data']['slot_to_roster_id']
    self.draft_id = draft_info['data']['draft_id']
    self.creators = draft_info['data']['creators']
    self.created = draft_info['data']['created']

  def picks(self) -> dict:
    picks_url = self.update_path(f"/draft/{self.draft_id}/picks")
    return (self.send_request(picks_url, None))

  def traded_picks(self) -> dict:
    traded_picks_url = self.update_path(f"/draft/{self.draft_id}/traded_picks")
    return (self.send_request(traded_picks_url, None))
