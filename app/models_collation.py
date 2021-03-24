import app.blueprints as blueprints

def collate_models(blueprints):
    model_list = []
    for blueprint in blueprints:
        try:
            from blueprint import models
            model_list.append(models)
        except:
            pass
    return model_list

#iterate through blueprints
#if models, import models
#iterate through models
#collate as list
#pass to top level app db