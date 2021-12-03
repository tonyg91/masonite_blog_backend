"""BlogTableSeeder Seeder."""
from app.Blog import Blog
from masoniteorm.seeds import Seeder


class BlogTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        Blog.create({"title": "Post1", "body": "First post"})
        Blog.create({"title": "Post2", "body": "Second post"})
        Blog.create({"title": "Post3", "body": "Third post"})
