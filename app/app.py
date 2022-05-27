from aiohttp import web
import aiosqlite
import asyncio
import utils

app = web.Application()
routes = web.RouteTableDef()

# cache
courses = {'FP': {}, 'ASC': {}}

# db queries
select_query = 'SELECT * FROM courses'
insert_query = 'INSERT INTO courses (course, date_time, name) VALUES (?, ?, ?)'
delete_query = 'DELETE FROM courses WHERE course = ? AND name = ?'

async def populate_cache():
    async with db.execute(select_query) as cursor:
        response = await cursor.fetchall()

    for r in response:
        course, date_time, name = r
        await insert_data(course, date_time, name, boot=True)

async def insert_data(course, hours, name, *, boot=False):
    data = courses.get(course)
    for key, value in list(data.items()):
        if name in value:

            # delete from db
            await db.execute(delete_query, (course, name,))
            await db.commit()
            
            value.remove(name)
            if not value:
                del data[key]

    if hours.lower() == 'delete':
        return

    if not data:
        data[hours] = [name]

    else:
        h = data.get(hours)
        if h is None:
            data[hours] = [name]

        else:
            if len(data[hours]) == 15:
                raise Exception('maximum people due to covid-19')

            data[hours].append(name)

    # insert to db
    # we do not need to insert to db on populate_cache
    if not boot:
        await db.execute(insert_query, (course, hours, name,))
        await db.commit()

@routes.post('/submit')
async def submit(request):
    data = await request.post()
    
    name = data['name']
    course, hours = data['select'].split('_')
    
    # ugly error handler, might rewrite later
    try:
        await insert_data(course, hours, name)
    except Exception as e:
        success = 'false'
    else:
        success = 'true'

    return web.HTTPFound(f'/?success={success}')

@routes.get('/results')
async def results(request):
    table = utils.create_table(courses)
    return web.Response(
        text=utils.table.format(body=table),
        content_type='text/html'
    )

if __name__ == '__main__':
    # startup
    loop = asyncio.get_event_loop()
    db = loop.run_until_complete(aiosqlite.connect('courses.db'))
    loop.create_task(populate_cache())

    app.add_routes(routes)
    web.run_app(app, port=2020)
