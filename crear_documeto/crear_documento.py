from appy.pod.renderer import Renderer

staff = [{'firstName': 'Delannay', 'name': 'Gaetan', 'age': 112},
         {'firstName': 'Gauthier', 'name': 'Bastien', 'age': 5},
         {'firstName': 'Jean-Michel', 'name': 'Abe', 'age': 79}]

print( globals() )
renderer = Renderer('repote_por_depenedencia.ods', globals(), 'result.ods')
renderer.run()