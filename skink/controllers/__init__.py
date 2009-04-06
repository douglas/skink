#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys
from os.path import dirname, abspath, join, exists
root_path = abspath(join(dirname(__file__), "../../"))
sys.path.insert(0, root_path)

import cherrypy

from skink.models import metadata, setup_all, drop_all
from skink.repositories import ProjectRepository
import template

class ProjectController(object):
    @cherrypy.expose
    @template.output("create_project.html")
    def new(self):
        return template.render()

    @cherrypy.expose
    def create(self, name, build_script):
        repository = ProjectRepository()
        project = repository.create(name=name, build_script=build_script)
        raise cherrypy.HTTPRedirect('/')

class IndexController(object):
    project = ProjectController()
    
    @cherrypy.expose
    @template.output("index.html")
    def index(self):
        repository = ProjectRepository()
        projects = repository.get_all()
        return template.render(projects=projects)