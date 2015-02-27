# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('condition', models.CharField(max_length=1, choices=[('a', 'Pristine'), ('b', 'Used, good'), ('c', 'Used, worn'), ('d', 'Cracked / chipped'), ('e', 'Broken')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Documentation',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('documentation_name', models.CharField(max_length=45, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='documentation_link_piece',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('documentation_date', models.DateField(blank=True, null=True)),
                ('documentation_author', models.CharField(max_length=45, blank=True)),
                ('documentation_media', models.CharField(max_length=45, blank=True)),
                ('documentation_location', models.CharField(max_length=45, blank=True)),
                ('documentation', models.ForeignKey(to='djapp.Documentation')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Exhibition',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('exhibition_name', models.CharField(max_length=45, blank=True)),
                ('exhibition_date', models.DateField(blank=True, null=True)),
                ('exhibition_description', models.CharField(max_length=1000, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='glaze_link_piece',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GlazeLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('glaze_name', models.CharField(max_length=45, blank=True)),
                ('glaze_description', models.CharField(max_length=500, blank=True)),
                ('glaze_begin_date', models.DateField(blank=True, null=True)),
                ('glaze_end_date', models.DateField(blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='heath_line_link_piece',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HeathLineLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('heath_line_name', models.CharField(max_length=45, blank=True)),
                ('heath_line_begin_date', models.DateField(blank=True, null=True)),
                ('heath_line_end_date', models.DateField(blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='maker_link_piece',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MakerLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('maker_name', models.CharField(max_length=45, blank=True)),
                ('maker_location', models.CharField(max_length=45, blank=True)),
                ('maker_start_date', models.DateField(blank=True, null=True)),
                ('maker_stop_date', models.DateField(blank=True, null=True)),
                ('maker_description', models.CharField(max_length=200, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='material_link_piece',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MaterialLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('material_name', models.CharField(max_length=45, blank=True)),
                ('material_description', models.CharField(max_length=100, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='method_link_piece',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MethodLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('method_name', models.CharField(max_length=45, blank=True)),
                ('method_description', models.CharField(max_length=500, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('catalogue_id', models.CharField(max_length=45)),
                ('heath_id', models.CharField(max_length=45, blank=True)),
                ('piece_name', models.CharField(max_length=45, blank=True)),
                ('piece_description', models.CharField(max_length=2000, blank=True)),
                ('manufactured_date', models.DateField(blank=True, null=True)),
                ('length_inches', models.IntegerField(blank=True, null=True)),
                ('width_inches', models.IntegerField(blank=True, null=True)),
                ('height_inches', models.IntegerField(blank=True, null=True)),
                ('weight_ounces', models.IntegerField(blank=True, null=True)),
                ('length_mm', models.IntegerField(blank=True, null=True)),
                ('width_mm', models.IntegerField(blank=True, null=True)),
                ('height_mm', models.IntegerField(blank=True, null=True)),
                ('weight_grams', models.IntegerField(blank=True, null=True)),
                ('cataloguer', models.CharField(max_length=45, blank=True)),
                ('catalogue_date', models.DateField(blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('Logo_name', models.CharField(max_length=45, blank=True)),
                ('Piece', models.OneToOneField(to='djapp.Piece', serialize=False, primary_key=True)),
                ('logo_description', models.CharField(max_length=200, blank=True)),
                ('stamp_name', models.CharField(max_length=45, blank=True)),
                ('picture', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('publication_name', models.CharField(max_length=45, blank=True)),
                ('publication_date', models.DateField(blank=True, null=True)),
                ('publication_author', models.CharField(max_length=45, blank=True)),
                ('publication_media', models.CharField(max_length=45, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SetCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('set_collection_name', models.CharField(max_length=45, blank=True)),
                ('setcollection_location', models.CharField(max_length=45, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='setCollection_link_piece',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('description', models.CharField(max_length=1000, blank=True)),
                ('Piece', models.ForeignKey(to='djapp.Piece')),
                ('SetCollection', models.ForeignKey(to='djapp.SetCollection')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='setcollection',
            name='set_collection_piece',
            field=models.ManyToManyField(through='djapp.setCollection_link_piece', to='djapp.Piece'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='piece',
            name='exhibition',
            field=models.ForeignKey(to='djapp.Exhibition'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='piece',
            name='publication',
            field=models.ForeignKey(to='djapp.Publication'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='methodlookup',
            name='method_pieces',
            field=models.ManyToManyField(through='djapp.method_link_piece', to='djapp.Piece'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='method_link_piece',
            name='MethodLookup',
            field=models.ForeignKey(to='djapp.MethodLookup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='method_link_piece',
            name='Piece',
            field=models.ForeignKey(to='djapp.Piece'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='materiallookup',
            name='material_pieces',
            field=models.ManyToManyField(through='djapp.material_link_piece', to='djapp.Piece'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='material_link_piece',
            name='MaterialLookup',
            field=models.ForeignKey(to='djapp.MaterialLookup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='material_link_piece',
            name='Piece',
            field=models.ForeignKey(to='djapp.Piece'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='makerlookup',
            name='maker_pieces',
            field=models.ManyToManyField(through='djapp.maker_link_piece', to='djapp.Piece'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='maker_link_piece',
            name='MakerLookup',
            field=models.ForeignKey(to='djapp.MakerLookup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='maker_link_piece',
            name='Piece',
            field=models.ForeignKey(to='djapp.Piece'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='heathlinelookup',
            name='heath_line_pieces',
            field=models.ManyToManyField(through='djapp.heath_line_link_piece', to='djapp.Piece'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='heath_line_link_piece',
            name='heath_line',
            field=models.ForeignKey(to='djapp.HeathLineLookup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='heath_line_link_piece',
            name='piece',
            field=models.ForeignKey(to='djapp.Piece'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='glazelookup',
            name='glaze_pieces',
            field=models.ManyToManyField(through='djapp.glaze_link_piece', to='djapp.Piece'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='glaze_link_piece',
            name='glaze',
            field=models.ForeignKey(to='djapp.GlazeLookup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='glaze_link_piece',
            name='piece',
            field=models.ForeignKey(to='djapp.Piece'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='documentation_link_piece',
            name='piece',
            field=models.ForeignKey(to='djapp.Piece'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='documentation',
            name='documentation_pieces',
            field=models.ManyToManyField(through='djapp.documentation_link_piece', to='djapp.Piece'),
            preserve_default=True,
        ),
    ]
