# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Projeto.created'
        db.add_column(u'erp_projeto', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 9, 26, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Projeto.modified'
        db.add_column(u'erp_projeto', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 9, 26, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Projeto.created'
        db.delete_column(u'erp_projeto', 'created')

        # Deleting field 'Projeto.modified'
        db.delete_column(u'erp_projeto', 'modified')


    models = {
        u'erp.apontamento': {
            'Meta': {'object_name': 'Apontamento'},
            'data': ('django.db.models.fields.DateField', [], {}),
            'funcionario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['erp.Funcionario']"}),
            'horas': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'projeto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['erp.Projeto']"})
        },
        u'erp.arquivo': {
            'Meta': {'object_name': 'Arquivo'},
            'arquivo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'projeto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['erp.Projeto']"})
        },
        u'erp.cliente': {
            'Meta': {'object_name': 'Cliente'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'erp.contato': {
            'Meta': {'object_name': 'Contato'},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['erp.Cliente']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'erp.customensal': {
            'Meta': {'object_name': 'CustoMensal'},
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['erp.Empresa']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'valor': ('django.db.models.fields.IntegerField', [], {})
        },
        u'erp.empresa': {
            'Meta': {'object_name': 'Empresa'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '33'})
        },
        u'erp.funcionario': {
            'Meta': {'object_name': 'Funcionario'},
            'carga_mensal': ('django.db.models.fields.IntegerField', [], {}),
            'cargo': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'gestor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'salario': ('django.db.models.fields.FloatField', [], {})
        },
        u'erp.projeto': {
            'Meta': {'object_name': 'Projeto'},
            'anexo_cronograma': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'anexo_escopo': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'anexo_orcamento': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'anexo_proposta': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'custos_extra': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'data_aceite_escopo': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'data_aceite_proposta': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'data_entrega': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'data_entrega_cliente': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'data_entrega_interna': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'data_entrega_orcamento': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'data_envio_escopo': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'data_envio_proposta': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'data_fim_ajustes_internos': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'data_inicio': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'data_inicio_real': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'data_solicitacao': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'descricao': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'descricao_escopo': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'descricao_orcamento': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['erp.Cliente']", 'null': 'True'}),
            'estimativa_horas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'recursos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['erp.Funcionario']", 'symmetrical': 'False', 'blank': 'True'}),
            'solicitante': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['erp.Contato']", 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'sc'", 'max_length': '2'}),
            'tipo_escopo': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'valor_cobrado': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'valor_liquido': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['erp']