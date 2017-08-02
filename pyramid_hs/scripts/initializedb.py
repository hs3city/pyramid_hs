import os
import sys
import transaction
from datetime import date

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from pyramid_hs.models.mymodel import Person, Pet
from ..db import db
from ..models import MyModel


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)

    with transaction.manager:
        db.create_tables([MyModel, Person, Pet], safe=True)
        Person.create(name='Bob', birthday=date(year=1960, month=5, day=1), is_relative=False)
