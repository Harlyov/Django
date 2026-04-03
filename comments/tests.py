from django.test import TestCase
from model_bakery import baker
from comments.models import Comment
from matches.models import Match
from fans.models import Fan

class CommentsModelTests(TestCase):
    def test_comment_creation_with_fk(self):
        match = baker.make(Match)
        fan = baker.make(Fan)
        comment = baker.make(Comment, match=match, fan=fan)
        self.assertEqual(comment.match, match)
        self.assertEqual(comment.fan, fan)