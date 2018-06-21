import sys
import random
import os

_valid_char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890_'
_valid_char_len = len(_valid_char)
_out_dir = "%s/%s" %( os.getcwd().replace('\\', '/') , 'rcode')

def query(tips):
    return raw_input( tips ).replace('\r', '')

def rand_int(min, max):
    range = max - min
    if min >= max:
        range = max
        min = 0
    if range == 0:
        return 0
    return int(random.random() * 10000000 ) % range + min;

def rand_str():
    len = rand_int(2, 32);
    str = ''
    for i in range(0, len):
        idx = rand_int(0, _valid_char_len)
        str = str + _valid_char[idx]
    return str

def generate_class_def(idx):
    cls_def = {}
    # class name
    cls_def['name'] = 'c_' + rand_str()
    cls_def['int_members'] = []
    cls_def['str_members'] = []
    cls_def['bool_members'] = []    
    cls_def['int_func'] = []
    cls_def['str_func'] = []
    cls_def['bool_func'] = []
    #class member
    for i in range(0, rand_int(0, 15)):
        mname =  'm_i' + str (i) + rand_str()
        if (cls_def['int_members'].count(mname) == 0):
            cls_def['int_members'].append( mname )

    for i in range(0, rand_int(0, 15)):
        mname =  'm_str' + str (i) + rand_str()
        if (cls_def['str_members'].count(mname) == 0):
            cls_def['str_members'].append(mname)

    for i in range(0, rand_int(0, 15)):
        mname = 'm_b' + str (i) + rand_str()
        if (cls_def['bool_members'].count(mname) == 0):
            cls_def['bool_members'].append(mname)

    for i in range(0, rand_int(0, 15)):
        fname = 'f_int' + str (i) + rand_str()
        if (cls_def['int_func'].count(fname) == 0):
            cls_def['int_func'].append( fname )

    for i in range(0, rand_int(0, 15)):
        fname = 'f_str' + str (i) + rand_str()
        if (cls_def['str_func'].count(fname) == 0):
            cls_def['str_func'].append( fname )

    for i in range(0, rand_int(0, 15)):
        fname = 'b_b' + str (i) + rand_str()
        if (cls_def['bool_func'].count(fname) == 0):
            cls_def['bool_func'].append( fname )
    

    return cls_def

def generate_class_header(cls_info):
    print( 'generate header %s' % (cls_info['name']) )
    fpath = "%s/%s.h" % (_out_dir , cls_info['name'] ) 
    fp = open(fpath, 'w+')
    fp.write( "#pragma once\r\n" )
    fp.write( "#include <string>\r\n" )

    fp.write( "class %s {\r\n" % (cls_info['name']) )
    # 
    fp.write( "public:\r\n" )
    fp.write( "\t%s();\r\n"  % (cls_info['name']) )    
    fp.write( "\t~%s();\r\n"  % (cls_info['name']) )
    fp.write( "\tvoid print_some_thing();\r\n")
    fp.write( "\r\n" )

    # member    
    fp.write( "public:\r\n" )
    for var in cls_info['int_members']:
        fp.write( "\tint %s;\r\n" % ( var ) )
    
    for var in cls_info['bool_members']:
        fp.write( "\tbool %s;\r\n" % (var ) )

    for var in cls_info['str_members']:
        fp.write( "\tstd::string %s;\r\n" % ( var ) )

    # member getter setter    
    fp.write( "public:\r\n" )
    for var in cls_info['int_members']:
        fp.write( "\tint get_%s();\r\n" % ( var  ))
        fp.write( "\tvoid set_%s(int val);\r\n" % ( var  ))
        fp.write( "\r\n" )
    
    for var in cls_info['bool_members']:
        fp.write( "\tbool get_%s();\r\n" % ( var  ))
        fp.write( "\tvoid set_%s(bool val);\r\n" % ( var  ))
        fp.write( "\r\n" )

    for var in cls_info['str_members']:
        fp.write( "\tstd::string get_%s();\r\n" % ( var  ))
        fp.write( "\tvoid set_%s(std::string val);\r\n" % ( var  ))
        fp.write( "\r\n")

    # func
    fp.write( "public:\r\n" )
    for var in cls_info['int_func']:
        fp.write( "\tint %s();\r\n" % ( var ) )
    
    for var in cls_info['bool_func']:
        fp.write( "\tbool %s();\r\n" % (var ) )

    for var in cls_info['str_func']:
        fp.write( "\tstd::string %s();\r\n" % ( var ) )
    
    fp.write('};')
    
    fp.close()

    
    return True

def generate_class_impl(cls_info):
    cls_name = cls_info['name']
    print( 'generate impl %s' % (cls_name) )
    fpath = "%s/%s.cpp" % (_out_dir , cls_name ) 
    fp = open(fpath, 'w+')
    fp.write( "// implement %s\r\n" % (cls_name) )
    fp.write( "#include \"%s.h\"\r\n" % (cls_name) )
    fp.write( "#include <string>\r\n" )
    fp.write( "#include <stdio.h>\r\n" )

    #impl
    callallfunc = []
   
    # member getter setter    
    for var in cls_info['int_members']:
        fp.write( "int %s::get_%s() {\r\n\treturn %s;\r\n}\r\n" % (cls_name, var ,var ))
        fp.write( "void %s::set_%s(int val){\r\n\t%s = val;\r\n}\r\n" % (cls_name, var ,var ))
        fp.write( "\r\n" )
        callallfunc.append( "set_%s(get_%s());" % (var ,var ))
    
    for var in cls_info['bool_members']:
        fp.write( "bool %s::get_%s() {\r\n\treturn %s;\r\n}\r\n" % (cls_name, var ,var ))
        fp.write( "void %s::set_%s(bool val){\r\n\t%s = val;\r\n}\r\n" % (cls_name, var ,var ))        
        callallfunc.append( "set_%s(get_%s());" % (var ,var ))

    for var in cls_info['str_members']:
        fp.write( "std::string %s::get_%s() {\r\n\treturn %s;\r\n}\r\n" % (cls_name, var ,var ))
        fp.write( "void %s::set_%s(std::string val){\r\n\t%s = val;\r\n}\r\n" % (cls_name, var ,var ))        
        callallfunc.append( "set_%s(get_%s());" % (var ,var ))

    # func
    for func in cls_info['int_func']:
        retname = "__ret%s" % ( rand_str() )
        fp.write( "int %s::%s(){\r\n" % (cls_name, func ) )
        fp.write( "\tint %s = 0;\r\n" % ( retname ) )
        for var in cls_info['int_members']:
            fp.write( "\t\t%s += %d + %s;\r\n" % ( retname, rand_int(0, 0xffff ), var ))
        fp.write( "\treturn %s;" %( retname ) )
        fp.write( "}\r\n\r\n" )        
        callallfunc.append( "%s();" % ( func ))
    
    nr_of_int_func = len( cls_info['int_func'] )
    for func in cls_info['bool_func']:
        retname = "__ret%s" % ( rand_str() )
        fp.write( "bool %s::%s(){\r\n" % (cls_name, func ) )
        fp.write( "\tbool %s = false;\r\n" % ( retname ) )
        for var in cls_info['bool_members']:
            if nr_of_int_func > 0:
                fp.write( "\t%s &= (%s() != 0) && %s;\r\n" % ( retname, cls_info['int_func'][rand_int(0, nr_of_int_func -1 )], var ))
            else:
                fp.write( "\t%s &= (%d != 0) && %s;\r\n" % ( retname, rand_int(0, 0xffff ), var ))
        fp.write( "\treturn %s;\r\n" %( retname ) )
        fp.write( "}\r\n\r\n" )        
        callallfunc.append( "%s();" % ( func ))

    nr_of_str_member = len(cls_info['str_members'])
    for func in cls_info['str_func']:
        retname = "__ret%s" % ( rand_str() )
        fp.write( "std::string %s::%s(){\r\n" % (cls_name, func ) )
        fp.write( "\tstd::string %s = \"empty\";\r\n" % ( retname ) )
        if nr_of_str_member > 0:
            for i in range(nr_of_str_member):
                fp.write( "\t%s += %s;\r\n" % ( retname, cls_info['str_members'][rand_int(0, nr_of_str_member -1 )] ))
        else:
            fp.write( "\t%s += \"%s\";\r\n" % ( retname, rand_str() ))
        fp.write( "\treturn %s;\r\n" %( retname ) )
        fp.write( "}\r\n\r\n" )
        callallfunc.append( "%s();" % ( func ))
    

    fp.write( "\r\n" )
    fp.write( "void %s::print_some_thing() { printf(\"%s_impl\"); }\r\n" % (cls_name,cls_name ))
    fp.write( "%s::~%s(){}\r\n"  % (cls_name, cls_name) )   
    fp.write( "%s::%s(){\r\n"  % (cls_name, cls_name) )  
    # call all func
    for call in callallfunc:
        fp.write( "\t%s\r\n" % ( call ) )
    fp.write( "}\r\n\r\n" )

    fp.close()

    return True


def generate_class(idx):
    clsdef = generate_class_def(idx)
    generate_class_header(clsdef)
    generate_class_impl(clsdef)
    return clsdef


def generate_class_owner( clses ):
    fpath = "%s/owner.cpp" % (_out_dir ) 
    fp = open(fpath, 'w+')
    fp.write( "#include <string>\r\n" )
    for cls in clses:
        fp.write( "#include \"%s.h\"\r\n" % (cls['name']) )

    fp.write( "void impl_ref_to_all_class(){\r\n" )
    for cls in clses:
        cls_name = cls['name']
        cls_ins = "__obj_%s" % (cls_name)
        fp.write( "\t%s* %s = new %s();\r\n" % (cls_name, cls_ins, cls_name) )    
        fp.write( "\t%s->print_some_thing();\r\n" % (cls_ins) )    
        fp.write( "\tdelete %s; \r\n\t%s=NULL;\r\n" % (cls_ins, cls_ins) )    

    fp.write( "}\r\n\r\n" )        

    fp.close()


def traverse_rm( dir ):  
    fs = os.listdir(dir)  
    for f in fs:  
        path = os.path.join(dir,f)  
        if not os.path.isdir(path):  
            os.remove(path)
        else:  
            traverse_rm(path)  
            os.rmdir(path)

if __name__ == '__main__':
    print _out_dir
    if os.path.isdir(_out_dir):
        traverse_rm(_out_dir)
        os.rmdir(_out_dir)
    os.mkdir(_out_dir)
    
    clses = []
    nr_of_cls = int( query('Number of random classes:') )
    for i in range(0, nr_of_cls):
        clses.append(generate_class( i ))

    generate_class_owner(clses);
        