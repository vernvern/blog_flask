import sys
import glob
import yaml
import inspect
from blog import db


def get_cls(table):
    module = sys.modules['blog.models.{0}'.format(table)]
    obj = ''.join([x.capitalize() for x in table.split('_')])
    cls = getattr(module, obj)
    return cls


def load_data():
    # 遍历yml文件
    for yml in glob.glob('./blog/fixture/*.yml'):
        objs = []
        with open(yml, 'r') as f:
            data_list = yaml.load(f)
            # 遍历文件内的数据块
            for data in data_list:
                table = data['table']
                some = data['list']
                cls = get_cls(table)
                # 遍历某数据块的一条数据
                for one in some:
                    obj = cls()
                    # 赋值
                    for k, v in one.items():
                        # 去重
                        if k == 'id' and cls.query.filter_by(id=v).first():
                            break
                        else:
                            setattr(obj, k, v)
                    else:
                        objs.append(obj)
        db.session.add_all(objs)
        db.session.commit()


if __name__ == '__main__':
    load_data()
