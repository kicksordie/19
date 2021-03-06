db=DAL('sqlite://storage.sqlite', pool_size=1, check_reserved=['all'])

from gluon.tools import Auth
auth = Auth(db)
auth.define_tables(username=True)

db.define_table('pr',
                Field('name'),
                format='%(name)s')

db.define_table('search_pr',
                 Field('Name', 'reference pr'),
                 format='%(Name)s')

db.define_table('Prof_rate',
                Field('Name', 'reference pr'),
                Field('Title', readable=False, writable=False),
                Field('Clarity'),
                Field('Easiness'),
                Field('Workload'),
                Field('Helpfulness'),
                Field('Counter', default=1, readable=False, writable=False))

db.define_table('Prof_data',
                Field('Title', 'reference pr'),
                Field('name', readable=False, writable=False),
                Field('Counter'),
                Field('Total_Clarity'),
                Field('Avg_Clarity'),
                Field('Total_Easiness'),
                Field('Avg_Easiness'),
                Field('Total_Workload'),
                Field('Avg_Workload'),
                Field('Total_Helpfulness'),
                Field('Avg_Helpfulness'))


db.define_table('course',
                Field('name'),
                Field('course_description','text'),
                Field('counter', default=0, readable=False, writable=False),
                format='%(name)s')

db.define_table('search_course',
                Field('Title', 'reference course'),
                format='%(Title)s')

db.define_table('Course_rate',
                Field('name', readable=False, writable=False),
                Field('Title', 'reference course'),
                Field('Comprehensibility', label='Learnability'),
                Field('Easiness'),
                Field('Struggle_Level', label='Workload'),
                Field('Relativity', label='Relevance'),
                Field('Counter', default=1, readable=False, writable=False))


db.define_table('Course_data',
                Field('Title', 'reference course'),
                Field('name', readable=False, writable=False),
                Field('Counter'),
                Field('Total_Comprehensibility'),
                Field('Avg_Comprehensibility'),
                Field('Total_Easiness'),
                Field('Avg_Easiness'),
                Field('Total_Struggle_Level'),
                Field('Avg_Struggle_Level'),
                Field('Total_Relativity'),
                Field('Avg_Relativity'))

db.define_table('comments',
                Field('Course_name', readable=False, writable=False),
                Field('Professor_name', readable=False, writable=False),
                Field('Username', writable=False),
                Field('Body', 'text'))

db.Prof_rate.Clarity.requires = IS_IN_SET(('0','1', '2', '3', '4','5'))
db.Prof_rate.Easiness.requires = IS_IN_SET(('0','1', '2', '3', '4','5'))
db.Prof_rate.Workload.requires = IS_IN_SET(('0','1', '2', '3', '4','5'))
db.Prof_rate.Helpfulness.requires = IS_IN_SET(('0','1', '2', '3', '4','5'))
db.Course_rate.Comprehensibility.requires = IS_IN_SET(('0','1', '2', '3', '4','5'))
db.Course_rate.Easiness.requires = IS_IN_SET(('0','1', '2', '3', '4','5'))
db.Course_rate.Struggle_Level.requires = IS_IN_SET(('0','1', '2', '3', '4','5'))
db.Course_rate.Relativity.requires = IS_IN_SET(('0','1', '2', '3', '4','5'))
#db.comments.Username.default=auth.user.username
