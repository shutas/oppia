# Copyright 2012 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Controllers for Oppia exploration statistics page."""

__author__ = 'sll@google.com (Sean Lip)'

from controllers.base import BaseHandler, require_editor
from models.statistics import Statistics, STATS_ENUMS


class StatsHandler(BaseHandler):
    """Handles display of the statistics page for explorations."""

    @require_editor
    def get(self, unused_user, exploration):
        """Displays the statistics page for the given exploration."""

        num_visits = Statistics.get_exploration_stats(
            STATS_ENUMS.exploration_visited, exploration.hash_id)

        num_completions = Statistics.get_exploration_stats(
            STATS_ENUMS.exploration_completed, exploration.hash_id)

        answers = Statistics.get_exploration_stats(
            STATS_ENUMS.default_case_hit, exploration.hash_id)

        self.values.update({
            'exploration_title': exploration.title,
            'exploration_id': exploration.hash_id,
            'num_visits': num_visits,
            'num_comp': num_completions,
            'answers': answers,
        })

        self.render_template('stats.html')
