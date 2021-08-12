# Generated by Django 2.1.7 on 2019-03-25 18:56

from django.db import migrations


def make_nodes(apps, schema_editor):
    from treebeard.mp_tree import MP_Node

    def _inc_path(path):
        """:returns: The path of the next sibling of a given node path."""
        newpos = MP_Node._str2int(path[-MP_Node.steplen :]) + 1
        key = MP_Node._int2str(newpos)
        if len(key) > MP_Node.steplen:
            raise Exception("Path Overflow from")
        return "{0}{1}{2}".format(
            path[: -MP_Node.steplen],
            MP_Node.alphabet[0] * (MP_Node.steplen - len(key)),
            key,
        )

    def add_children(leaf, children):
        leaf.numchild += len(children)
        leaf.save()
        last_child = None
        for child in children:
            child.depth = leaf.depth + 1
            if last_child is None:
                child.path = MP_Node._get_path(leaf.path, child.depth, 1)
            else:
                child.path = _inc_path(last_child.path)
            child.save()
            last_child = child
            sub_children = GeoRegion.objects.filter(part_of=child).order_by("name")
            add_children(child, sub_children)

    GeoRegion = apps.get_model("georegion", "GeoRegion")

    root_regions = GeoRegion.objects.filter(part_of__isnull=True).order_by("name")
    last_root = None
    for georegion in root_regions:
        if last_root is None:
            newpath = MP_Node._get_path(None, 1, 1)
        else:
            newpath = _inc_path(last_root.path)

        georegion.depth = 1
        georegion.path = newpath
        georegion.save()
        last_root = georegion

    for georegion in root_regions:
        children = GeoRegion.objects.filter(part_of=georegion).order_by("name")
        add_children(georegion, children)


class Migration(migrations.Migration):

    dependencies = [
        ("georegion", "0007_auto_20190325_1956"),
    ]

    operations = [migrations.RunPython(make_nodes)]
