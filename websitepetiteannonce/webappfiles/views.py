
from flask import Blueprint, render_template, request,flash, redirect, url_for, session

import re



import mysql.connector
from webappfiles.db import dbconnect
cur, con = dbconnect.get_connection() 

from datetime import datetime,timedelta 
import os

from flask_mail import Mail, Message
from . import mail

from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash






views = Blueprint('views', __name__)
#referring to the default page via the “/” route



#-------------------------------ADMIN---------------------------------------------------------------------------------------------------------------------------------------------------


@views.route("/adminhome/")
def adminhome():
    if 'adminid' in session and  'fn' in session  :
        admin_id = session['adminid']
        fn = session['fn']
        cur.execute("SELECT COUNT(*) FROM tbluser")
        rows = cur.fetchone()[0]
        return render_template("adminhome.html", admin_id=admin_id,fn=fn,rows=rows)
    else:
        flash('Please log in.', category='error')
        return redirect(url_for('views.logg'))
    

@views.route("/loginn/",methods=['GET', 'POST'])
def logg():
    try:
        
        if request.method == 'POST':
            email = request.form['txtemail']
            pwd = request.form['txtpass']

            login_admin = " select password, admin_id, username FROM tbladmin WHERE email=%s"
            val = (email,)
            cur.execute(login_admin, val)
            rows = cur.fetchall()
            count = cur.rowcount

            for row in rows:
                passw = row[0]

            if count > 0:
                if (passw== pwd):
                    session["adminid"] = rows[0][1]
                    session["fn"] = rows[0][2]
                    
                    
                    flash('Logged in successfully!', category='success')
                    
                    return redirect(url_for('views.adminhome'))
                else:
        
                    return "Incorrect email or password, please try again.', category='error"
            else: 
                
                return "Incorrect email or password, please try again.', category='error"

    except Exception as e:
            con.rollback()
            msg = "Error!!Try again " + str(e)
    return render_template('loginadmin.html')

@views.route("/viewgraph/")
def view_graph():
    
   
    
    cur.execute("SELECT c.cat_type, COUNT(pa.product_id) FROM tblproduct_advert pa INNER JOIN tblcategory c ON c.catid = pa.cat_id GROUP BY c.cat_type")
    data = cur.fetchall()
    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    cur.execute("SELECT u.id, u.username, COUNT(pa.product_id) FROM tbluser u INNER JOIN tblproduct_advert pa ON u.id = pa.id GROUP BY u.id, u.username ORDER BY COUNT(pa.product_id) DESC")
    data1 = cur.fetchall()
    labels1 = [row[1] for row in data1]
    values1 = [row[2] for row in data1]

    cur.execute("SELECT u.id, u.username, COUNT(sa.s_id) FROM tbluser u INNER JOIN tblservice_advert sa ON u.id = sa.s_id GROUP BY u.id, u.username ORDER BY COUNT(sa.s_id) DESC")
    data2 = cur.fetchall()
    labels2 = [row[1] for row in data2]
    values2 = [row[2] for row in data2]

    return render_template("graph.html", labels2=labels2, values2=values2, labels=labels, values=values, labels1=labels1, values1=values1)

            


@views.route('/categoryy/', methods=['GET', 'POST'])
def categories():
    if request.method == 'POST':
        if 'category_id' in request.form:
            category_id = request.form['category_id']
            new_name = request.form['category_type']
            
            if category_id:
                try:
                    category_id = int(category_id)
                    update_cat = "UPDATE tblcategory SET cat_type = %s WHERE catid = %s"
                    update_cat1 = (new_name, category_id)
                    cur.execute(update_cat, update_cat1)
                    con.commit()
                    return redirect('/categoryy/')
                except ValueError:
                    flash("Error: Invalid category_id value", category="error")
                except Exception as e:
                    con.rollback()
                    flash("Error: " + str(e), category="error")
            else:
                 flash("Error: category_id is required", category="error")
        else:
            
            new_name = request.form['category_type']
            
            existing_category = "SELECT * FROM tblcategory WHERE cat_type = %s"
            val1 = (new_name,)
            cur.execute(existing_category,val1)
            existing_category = cur.fetchone()
            
            if existing_category:
                flash("Error: Category already exists", category="error")
                
            else:
                try:
                    insert_cat = "INSERT INTO tblcategory (cat_type) VALUES (%s)"
                    val2 = (new_name,)
                    cur.execute(insert_cat, val2)
                    con.commit()
                    flash("Category added successfully!", category="success")
                    return redirect('/categoryy/')
                except Exception as e:
                    con.rollback()
                    flash("Error: " + str(e), category="error")
    else:
        try:
            cur.execute("SELECT * FROM tblcategory")
            categories = cur.fetchall()
            return render_template("category.html", categories=categories)
        except Exception as e:
           flash("Error: " + str(e), category="error")
    return redirect('/categoryy/')
        
@views.route('/categoryy/delete', methods=['POST'])
def delete_category():
    category_id = request.form.get('category_id')
    
    if category_id:
        try:
            category_id = int(category_id)
            delete_cat = "DELETE FROM tblcategory WHERE catid = %s"
            delete_cat1 = (category_id,)
            cur.execute(delete_cat, delete_cat1)
            con.commit()
            return redirect('/categoryy/')
        except ValueError:
           flash("Error: " + str(e), category="error")
        except Exception as e:
            con.rollback()
            flash("Error: " + str(e), category="error")
    else:
       flash("Error: category_id is required", category="error")
       return redirect('/category/')
    
    
    
        
    
@views.route("/viewuser/", methods=['GET', 'POST'])
def view_user():
    rows=[]
    msg=""
    if request.method == 'POST':
        id = request.form['id']
        frozen = request.form['frozen']
        
        
        update_frozen = "UPDATE tbluser SET frozen = %s WHERE id = %s"
        cur.execute(update_frozen, (frozen, id))
        con.commit()
    lname = request.args.get("txtlname") 
    if lname:
        search_user = "SELECT * FROM tbluser ur INNER JOIN tbldisctrict lo ON ur.loc_id = lo.loc_id WHERE lname LIKE %s"
        cur.execute(search_user, ('%' + lname + '%',))
        rows = cur.fetchall()
        msg = str(cur.rowcount ) + " record added, "
    else:
        cur.execute("SELECT * FROM tbluser ur INNER JOIN tbldisctrict lo ON ur.loc_id = lo.loc_id")
        rows = cur.fetchall()
        
    return render_template("viewuser.html", rows=rows, msg=msg)

 



@views.route("/viewproduct/" ,methods=['GET', 'POST'])
def view_product():
    rows=[]
    msg=""
    
    if request.method == 'POST':
        productid = request.form['productid']
        status = request.form['status']
        
        
        
        sql = "SELECT u.email, u.fname FROM tbluser u INNER JOIN tblproduct_advert pa ON u.id = pa.id WHERE pa.product_id = %s"
        cur.execute(sql, (productid,))
        row = cur.fetchone()

        if row:
            email = row[0]
            fname = row[1]
            
            if status=="Approve":
             
                    msg1 = Message('PetiteAnnonce', sender = 'darshanasramroop@gmail.com',recipients = [email])

                    msg1.body = "Congratulation " + fname +"\r\n"

                    msg1.body += "Your advert has been approved\r\n "

                    mail.send(msg1)
                
            elif status=="Reject":
             
                    msg1 = Message('PetiteAnnonce', sender = 'darshanasramroop@gmail.com',recipients = [email])

                    msg1.body = "Sorry to inform you " + fname +"\r\n"

                    msg1.body += "Your advert has been rejected\r\n "

                
                    mail.send(msg1)
                
            
        
        
        update_status = "UPDATE tblproduct_advert SET status = %s WHERE product_id = %s"
        cur.execute(update_status, (status, productid))
        con.commit()
    
    
    status1 = request.args.get("status") 
    if status1:
        
            search_advert = "SELECT * FROM tblproduct_advert pa inner join tblcategory ca on\
                pa.cat_id=ca.catid  WHERE status LIKE %s"
            cur.execute(search_advert, ('%' + status1 + '%',))
            rows = cur.fetchall()
            msg = str(cur.rowcount ) + " record added, "
    else:
            cur.execute("select * from tblproduct_advert pa inner join tblcategory ca on\
            pa.cat_id=ca.catid ")
            rows = cur.fetchall()
    return render_template("listadvert.html", rows = rows,msg=msg)




@views.route("/viewservice/", methods=['GET', 'POST'])
def view_service():
    rows=[]
    msg=""
    
    if request.method == 'POST':
        serviceid = request.form['serviceid']
        status = request.form['status']
        
      
        sql = "SELECT u.email, u.fname FROM tbluser u INNER JOIN  tblservice_advert pa ON u.id = pa.id WHERE pa.s_id = %s"
        cur.execute(sql, (serviceid,))
        row = cur.fetchone()

        if row :
            email = row[0]
            fname = row[1]
            
            if status=="Approve":
             
                msg1 = Message('PetiteAnnonce', sender = 'darshanasramroop@gmail.com',recipients =[email])

                msg1.body = "Congratulation " + fname +"\r\n"

                msg1.body += "Your advert has been approved\r\n "

                mail.send(msg1)
                
            elif status=="Reject":
             
                msg1 = Message('PetiteAnnonce', sender = 'darshanasramroop@gmail.com',recipients = [email])

                msg1.body = "Sorry to inform you " + fname +"\r\n"

                msg1.body += "Your advert has been rejected\r\n "

                
                mail.send(msg1)
                
        
        
        update_status = "UPDATE tblservice_advert SET status = %s WHERE s_id = %s"
        cur.execute(update_status, (status, serviceid))
        con.commit()
    
    
    status1 = request.args.get("status") 
    if status1:
        
        search_advert = "select * from tblservice_advert pa inner join tblcategory ca on\
            pa.cat_id=ca.catid  WHERE status LIKE %s"
        cur.execute(search_advert, ('%' + status1 + '%',))
        rows = cur.fetchall()
        msg = str(cur.rowcount ) + " record added, "
    else:
        cur.execute("select * from tblservice_advert pa inner join tblcategory ca on\
            pa.cat_id=ca.catid ")
        rows = cur.fetchall()
    return render_template("listservice.html", rows = rows,msg=msg)


@views.route("/removeproduct/" ,methods=['GET'])
def remove_product():
    rows=[]
    msg=""
    
    try:
        
        if request.method == "GET":
            product_id = request.args.get("productid")
            if product_id is not None:
           
                delete_advert = "DELETE FROM tblproduct_advert WHERE product_id = %s "
                cur.execute(delete_advert, (product_id,))
                con.commit()
                flash("Product advert deleted successfully!", category='success')
            
    

            current = datetime.now().date()
            exp = current - timedelta(days=7)
            select_advert="SELECT * FROM tblproduct_advert WHERE expiry_date < %s and request=0"
            cur.execute(select_advert,(current,))
            rows = cur.fetchall()

           
        
    
    except Exception as e:
            flash( "Error: " + str(e))
    return render_template("removepadvert.html", rows = rows,msg=msg)


 
@views.route("/removeservice/" ,methods=['GET'])
def remove_service():
    rows=[]
    msg=""
    
    try:
        
        if request.method == "GET":
            service_id = request.args.get("serviceid")
            if service_id is not None:
                delete_advert = "DELETE FROM tblservice_advert WHERE s_id = %s "
                cur.execute(delete_advert, (service_id,))
                con.commit()
                flash("Service advert deleted successfully!", category='success')
                
                
                

        current = datetime.now().date()
        exp = current - timedelta(days=7)
        select_advert = "SELECT * FROM tblservice_advert WHERE expiry_date < %s and request=0"
        cur.execute(select_advert, (current,))
        rows = cur.fetchall()

    except Exception as e:
        flash("Error: " + str(e), category='error')

    return render_template("removesadvert.html", rows=rows, msg=msg)



 
@views.route("/adminrenewservice/" ,methods=['GET'])
def admin_service():
    rows=[]
    msg=""
    
    try:
        
        if request.method == "GET":
            service_id = request.args.get("productid")
            if service_id is not None:
                delete_advert = " update tblservice_advert set renew =1 where s_id = %s  "
                cur.execute(delete_advert, (service_id,))
                con.commit()
                flash("Service advert renewed successfully!", category='success')
                
                
                
              
                sql="SELECT u.email,u.fname FROM tblservice_advert AS pa INNER JOIN tbluser AS u ON pa.id = u.id WHERE pa.s_id = %s"
                cur.execute(sql,(service_id,))
                rows1=cur.fetchone()
                if rows1:
                    email = rows1[0]
                    fname = rows1[1]
                
               
                msg1 = Message('PetiteAnnonce', sender = 'darshanasramroop@gmail.com',recipients =[email])

                msg1.body = "Hello " + fname +"\r\n"

                msg1.body += "Your advert has been renewed\r\n "

                mail.send(msg1)
            
                
                update = "UPDATE tblservice_advert SET expiry_date = DATE_ADD(expiry_date, INTERVAL 7 DAY) WHERE s_id = %s"
                cur.execute(update, (service_id,))
                con.commit()

        current = datetime.now().date()
        exp = current - timedelta(days=7)
        select_advert = "SELECT * FROM tblservice_advert WHERE expiry_date < %s  and request=1"
        cur.execute(select_advert, (current,))
        rows = cur.fetchall()

    except Exception as e:
        flash("Error: " + str(e), category='error')

    return render_template("renewadminservice.html", rows=rows, msg=msg)




@views.route("/adminrenewproduct/" ,methods=['GET'])
def admin_product():
    rows=[]
    msg=""
    
    try:
        
        if request.method == "GET":
            product_id = request.args.get("productid")
            
            if product_id is not None:
           
                delete_advert = "update tblproduct_advert set renew =1 where product_id = %s "
                cur.execute(delete_advert, (product_id,))
                con.commit()
                flash("Product advert renew successfully!", category='success')
                
                
                sql="SELECT u.email,u.fname FROM tblproduct_advert AS pa INNER JOIN tbluser AS u ON pa.id = u.id WHERE pa.product_id = %s"
                cur.execute(sql,(product_id,))
                rows1=cur.fetchone()
                if rows1:
                    email = rows1[0]
                    fname = rows1[1]
                
               
                msg1 = Message('PetiteAnnonce', sender = 'darshanasramroop@gmail.com',recipients =[email])

                msg1.body = "Hello " + fname +"\r\n"

                msg1.body += "Your advert has been renewed\r\n "

                mail.send(msg1)
                
                
                update = "UPDATE tblproduct_advert SET expiry_date = DATE_ADD(expiry_date, INTERVAL 7 DAY) WHERE product_id = %s"
                cur.execute(update, (product_id,))
                con.commit()
            
    
    

            current = datetime.now().date()
            exp = current - timedelta(days=7)
            select_advert="SELECT * FROM tblproduct_advert WHERE expiry_date < %s and request=1"
            cur.execute(select_advert,(current,))
            rows = cur.fetchall()

           
        
    
    except Exception as e:
            flash( "Error: " + str(e))
    return render_template("renewadminadvert.html", rows = rows,msg=msg)




 
 

@views.route('/logout/')
def logout():
    session.pop('adminid', None)
    return redirect('/home/')

#------------------------------Home--------------------------------------------------------------------------------------------------------------------------------------------------------------

 
@views.route("/home/")
def homee():
        if 'userid' in session and 'fn' in session:
            user_id = session['userid']
            fn = session['fn']
            return render_template("home.html", userid=user_id, fn=fn)
        else:
             flash('Please log in.', category='error')
        redirect(url_for('views.log'))
        return render_template("home.html")
       

@views.route("/about/")
def about():
    return render_template("about.html")

  
@views.route("/signupp/")
def sign():
    return render_template("usersignup.html") 
      
@views.route("/Registerdetails", methods=["POST"])
def registerdetails():
     if request.method == 'POST':
        email = request.form['txtemail']
        first_name = request.form['fname']
        last_name = request.form['lname']
        password1 = request.form['txtpass']
        user_name = request.form['username']
        #add the sql to search for the user by his email address
        sql = "select * from tbluser where email = %s"
        val = (email,)
        cur.execute(sql, val)
        rows = cur.fetchall()
        count = cur.rowcount
        if (count > 0):
            #add the flash category
            flash('Email already exists.', category='error')
        elif (len(first_name)< 3 ):
            flash('First name must be greater than 2 characters.', category="error")
        elif (re.search('^[a-z0-9]+[\._]?[a-z0-9]+@[A-Za-z0-9.-]+\.\w{2,3}$', email) is None):
            flash('Invalid email.', category="error")
        
        elif (len(password1)<3):
            flash('Password must be at least 3 characters.',  category="error")
        else:
            #add the encryption method
                #passw = generate_password_hash(password1, method='sha256')
                #add the attributes
                insert_user = "INSERT into tbluser (email, fname, lname,username,frozen,password) values (%s,%s,%s,%s,%s,%s)"
                val2 = (email, first_name, last_name,user_name,'active', password1)
                cur.execute(insert_user, val2)
                con.commit()
                #count the number of rows
                msg = str(cur.rowcount ) + " record added, "
                #set the sucess category flash message
                
                msg1 = Message('PetiteAnnonce', sender = 'darshanasramroop@gmail.com',
                recipients = [email])

                msg1.body = "Welcome to PetiteAnnonce " + first_name +"\r\n"

                msg1.body += "You are now a member and may access the website\r\n "

                msg1.body += "@ http://localhost:5000/home/"
                mail.send(msg1)
                msg = str(cur.rowcount ) + " record added, "
            #set the success category flash message
                flash(msg + ' account created!', category='success')
     return redirect(url_for('views.log'))
            
@views.route("/login/", methods=['GET', 'POST'])
def log():
    try:
        if request.method == 'POST':
            email = request.form['txtemail']
            pwd = request.form['txtpass']

            login_user = "SELECT id, lname, frozen,phone_number FROM tbluser WHERE email=%s AND password=%s"
            val = (email, pwd)

            cur.execute(login_user, val)
            rows = cur.fetchall()


            if len(rows) > 0:
                frozen = rows[0][2]

                if frozen == 'inactive':
                    flash("Your account has been frozen.", category='error')
                elif frozen == 'active':
                    # Password is correct
                    # Store session variables and redirect
                    session["userid"] = rows[0][0]
                    session["fn"] = rows[0][1]
                    session["email"] = email
                    session["phone"] = rows[0][3]

                    flash('Logged in successfully!', category='success')
                    return redirect(url_for('views.profile'))
                else: # User does not exist
                    flash("Incorrect email or password, please try again.", category='error')
            else:
                # Password is incorrect
                flash("Incorrect email or password, please try again.", category='error')

    except Exception as e:
        con.rollback()
        msg = "Error!! Try again " + str(e)
        print("Error in log function:", e)
    
    return render_template("login.html")

@views.route("/forgot/" ,methods=['POST','GET'])
def forgot_pass():
    
    if request.method == "POST":
        email = request.form.get("txtemail")
        sql1 = "select * from tbluser where email =%s"
        val1 = (email,)
        cur.execute(sql1, val1)
        rows = cur.fetchall()

        count = len(rows)
        count = cur.rowcount
        if count > 0:
            
            try:
  
                msg1 = Message('PetiteAnnonce', sender = 'darshanasramroop@gmail.com',recipients =[email])
                msg1.body = "It seems that you have forgot your password "
                msg1.body += "You can reset your password by clicking on the link below\r\n "
                msg1.body += f"http://localhost:5000/reset/{email}\n\n"
                msg1.body += " If You did not request to reset your password,please ignore this email\r\n "
                mail.send(msg1)
                flash("Password reset have been sent to your email.", category='success')
                return redirect(url_for('views.log'))
            
            except Exception as e:
                 flash("Error! . Please try again later.", category='error')

    else:
            flash("Email address not found. Please try again.", category='error')

    return render_template("forgotpass.html")
    
    
@views.route("/reset/<string:email>", methods=['GET', 'POST'])
def reset_pass(email):
    
    if not email:
        flash("Invalid password reset link. Please try again.", category='error')
        return redirect(url_for('views.forgot_pass'))
   
    if request.method == 'POST':
        pass1 = request.form.get('txtpass1')
        pass2 = request.form.get('txtpass2')

        if pass1 == pass2:
            try:
                update_pass = "UPDATE tbluser SET password = %s WHERE email = %s"
                val = (pass1, email)
                cur.execute(update_pass, val)
                
                con.commit()

                flash("Password successfully changed. Log in with your new password.", category='success')
                return redirect(url_for('views.log'))

            except Exception as e:
                con.rollback() 
                flash("Error!! Password reset failed. Please try again later.", category='error')

        else:
            flash("Passwords do not match. Please try again.", category='error')

    return render_template("reset.html", email=email, msg="")

@views.route("/modify/", methods=['GET', 'POST'])
def modify_pass():
    if 'userid' in session:
        if request.method == 'POST':
            pass2 = request.form['txtpass']
            pass3 = request.form['txtpass1']
            sql1="Select password from tbluser where id=%s"
            uid=session['userid']
            val1=(uid,)
            cur.execute(sql1, val1)
            rows=cur.fetchone()
            count=cur.rowcount
            
            for row in rows:
                passw=row[0]

            if count <1:
                flash("User with the given email not found. Password reset failed.", category='error')    
           
            elif pass2 != pass3:
                flash("New passwords do not match. Please try again.", category='error')
            elif pass2==pass3:
                sql2="Update tbluser set password=%s where id=%s"
                val2=(pass2,uid)
                cur.execute(sql2, val2)
                con.commit()

                flash("Password successfully changed. Log in with your new password.", category='success')
            
         
        return render_template("modifypass.html", msg="")
    else:
      return redirect(url_for('views.profile'))


@views.route("/addproduct/")
def add_product():
    if 'userid' in session:
        cur.execute("select * from tblcategory")
        rows1 = cur.fetchall()
   
    return render_template("addpadvert.html",rows1=rows1)

@views.route("/productdetails/", methods=["POST"])
def productDetails():
    if 'userid' in session:
        msg = "msg"
        if request.method == "POST":
            try:
            
                name = request.form["txtname"]
                descr = request.form["txtdesc"]
                price = request.form["txtprice"]
                utime = request.form["txtutime"]
                cat = request.form["ddlcat"]
                
            
                if "doc"  in request.files:
                    files=request.files.getlist("doc")
                    for file in files: 
                        file.save(os.path.join("webappfiles/static/images", file.filename))
              
                        filepath = os.path.join("/static/images", file.filename)
                        current_date = datetime.now().date()
                        exp_date = current_date + timedelta(days=7)

                        insert_p = "INSERT into tblproduct_advert (product_name,descr, price,  usage_time, status, expiry_date, document, cat_id,id) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                        val = (name, descr, price, utime, 'pending',exp_date, filepath, cat,session["userid"])
                        cur.execute(insert_p, val)
                        con.commit()

                        msg = str(cur.rowcount) + " advert added"

            
                        catid = request.form.getlist("cat")
                        lastbkid = cur.lastrowid
                        for cid in catid:
                            insert_cat = "INSERT INTO tblcategory(cat_type) VALUES ( %s)"
                            val2 = (lastbkid, cid)
                            cur.execute(insert_cat, val2)
                            con.commit()
                else:
                    msg = "Product cannot be added. Please upload all required files."

            except Exception as e:
                con.rollback()
                msg = "Product cannot be added " + str(e)

            finally:
                con.close()
                return render_template("addpadvert.html", msg=msg)

@views.route("/addservice/")
def add_service():
    if 'userid' in session:
        cur.execute("select * from tblcategory")
        rows1 = cur.fetchall()
   
    return render_template("addsadvert.html",rows1=rows1)

@views.route("/servicedetails/", methods=["POST"])
def serviceDetails():
    if 'userid' in session:
        msg = "msg"
        if request.method == "POST":
            try:
            
                name = request.form["txtname"]
                descr = request.form["txtdesc"]
                d = request.files["doc"]
                cat = request.form["ddlcat"]
           
                if d:
                    d.save(os.path.join(".\webappfiles\static\images", d.filename))
                    filepath = os.path.join("\static\images", d.filename)
                    
                    current_date = datetime.now().date()
                    exp_date = current_date + timedelta(days=7)
                    
                    sql = "INSERT into tblservice_advert (service_name, descr,status, expiry_date, document, cat_id,id) values (%s,%s,%s,%s,%s,%s,%s)"
                    val = (name, descr, 'pending',exp_date, filepath, cat,session["userid"])
                    cur.execute(sql, val)
                    con.commit()

                    msg = str(cur.rowcount) + " advert added"

                    catid = request.form.getlist("cat")
                    lastbkid = cur.lastrowid
                    for cid in catid:
                        sql2 = "INSERT INTO tblcategory(cat_type) VALUES (%s)"
                        val2 = (lastbkid, cid)
                        cur.execute(sql2, val2)
                        con.commit()
                else:
                     msg = "Product cannot be added. Please upload all required files."

            except Exception as e:
                con.rollback()
                msg = "Service cannot be added " + str(e)

            finally:
                con.close()
            return render_template("addsadvert.html", msg=msg)
        


@views.route('/logouttt/')
def logoutt():
    session.pop('userid', None)
    return redirect('/home/')
    
    
 

@views.route("/profile/")
def profile():
    if 'userid' in session:
        
        sql = "select * from tbluser where id = %s "
        val = (session['userid'],)
        cur.execute(sql, val)
        rows = cur.fetchall()
        session['fn']=rows[0][2]
        return render_template('updateprofile.html', rows=rows)
    else:
        return redirect('/home/')
    
@views.route("/updateprofile/", methods=["GET", "POST"])
def update_profile():
    if request.method == "POST":
        email = request.form['txtemail']
        first_name = request.form['txtfn']
        last_name = request.form['txtln']
        phone = request.form['txtphone']
        user_name = request.form['username']
        gender = request.form['txtgender']
        
        
        session['fn']=""
        try:
        
            sql = "update tbluser set email =%s, fname =%s, lname =%s, phone_number =%s,username=%s,gender=%s where id=%s "
            val = (email, first_name, last_name, phone,user_name,gender,session['userid'])
            cur.execute(sql, val)
            con.commit()
            msg = str(cur.rowcount) + " record successfully updated"
            flash(msg, category='success')
        except:
            msg = "Cannot be updated"
            flash(msg, category='error')
        finally:
            return redirect('/profile/')
    else:
        return redirect('/login/')
    
    
    
@views.route("/viewuseradvert/", methods=['GET', 'POST'])
def view_useradvert():
    rows = [] 
    rows1=[]
    if 'userid' in session:
        id=session.get('userid')
        
        current = datetime.now().date()
        
        view="select * from tblservice_advert pa inner join tbluser u on pa.id=u.id INNER JOIN tblcategory AS c ON pa.cat_id = c.catid where u.id=%s and pa.expiry_date >= %s "
        val=(id,current)
        cur.execute(view,val)
        rows = cur.fetchall()
        
        
        pview = "SELECT * FROM tblproduct_advert pa INNER JOIN tbluser u ON pa.id = u.id INNER JOIN tblcategory AS c ON pa.cat_id = c.catid WHERE u.id = %s and pa.expiry_date >= %s"
        cur.execute(pview, val)
        rows1 = cur.fetchall()
        
                
             
    return render_template("userviewadvert.html",rows=rows,rows1=rows1)

@views.route("/deleteservice/", methods=['GET', 'POST'])
def delete_service():
    if 'userid' in session:
        id=session.get('userid')
        s_id=request.form['serviceid']
        
        delete_type="Delete from tblservice_advert where s_id = %s AND id = %s"
        val=(s_id,id)
        cur.execute(delete_type,val)
        con.commit()
    return redirect('/viewuseradvert/')


@views.route("/deleteproduct/", methods=['GET', 'POST'])
def delete_product():
    if 'userid' in session:
        id=session.get('userid')
        p_id=request.form['productid']
        
        delete_type="Delete from tblproduct_advert where product_id=%s AND id = %s"
        val=(p_id,id)
        cur.execute(delete_type,val)
        con.commit()
    return redirect('/viewuseradvert/')


 
@views.route("/upservice/")
def up_service():
    if 'userid' in session:
        s_id = request.args.get('serviceid') 
        sql = "SELECT * FROM tblservice_advert WHERE s_id = %s AND id = %s"
        val = (s_id, )
        cur.execute(sql, val)
        rows = cur.fetchall()
        cur.execute("SELECT catid,cat_type FROM tblcategory")
        rows1 = cur.fetchall()
        
    return render_template('updateservice.html', rows=rows,rows1=rows1)
    
    
@views.route("/updateservice/", methods=["GET", "POST"])
def update_service():
    if 'userid' in session:
        user_id = session.get('userid')
        s_id = request.args.get('serviceid')
        rows=""
        rows1=""
        
        cur.execute("SELECT catid,cat_type FROM tblcategory")
        rows1 = cur.fetchall()
        
       
     
        sql = "SELECT * FROM tblservice_advert WHERE s_id = %s "
        val = (s_id,)
        cur.execute(sql, val)
        rows = cur.fetchall()
            
        try:
              
           
                
            if request.method == "POST":
                name= request.form['txtname']
                desr= request.form['txtdesc']
                doc = request.files.get('doc')
                cat = request.form["ddlcat"]
           
                if doc:
                    doc.save(os.path.join(".\webappfiles\static\images", doc.filename))
                    filepath = os.path.join("\static\images", doc.filename)
        
            
                updatep = "UPDATE tblservice_advert SET service_name = %s, descr = %s, document = %s, cat_id = %s WHERE s_id = %s "
                val = (name, desr, filepath,cat,s_id)
                cur.execute(updatep, val)
                con.commit()

                
                
                msg = str(cur.rowcount) + " record successfully updated"
                flash(msg, category='success')
                
              
                return redirect('/viewuseradvert/')
        except:
                
        
                msg = "Cannot be updated"
                flash(msg, category='error')
              
            
        return render_template("updateservice.html", rows=rows,rows1=rows1)
    else:
        return redirect('/login/')
    
    
    
    
     
@views.route("/upproduct/")
def pro_advert():
    if 'userid' in session:
        s_id = request.args.get('productid') 
        sql = "SELECT * FROM tblproduct_advert WHERE product_id = %s AND id = %s"
        val = (s_id, )
        cur.execute(sql, val)
        rows = cur.fetchall()
        cur.execute("SELECT catid,cat_type FROM tblcategory")
        rows1 = cur.fetchall()
        
    return render_template('updateproduct.html', rows=rows,rows1=rows1)
    
    
@views.route("/updateproduct/", methods=["GET", "POST"])
def update_product():
    if 'userid' in session:
        user_id = session.get('userid')
        s_id = request.args.get('productid')
        rows=""
        rows1=""
        
        cur.execute("SELECT catid,cat_type FROM tblcategory")
        rows1 = cur.fetchall()
        
       
     
        sql = "SELECT * FROM tblproduct_advert WHERE product_id = %s "
        val = (s_id,)
        cur.execute(sql, val)
        rows = cur.fetchall()
            
        try:
              
           
                
            if request.method == "POST":
                name= request.form['txtname']
                desr= request.form['txtdesc']
                price= request.form['txtprice']
                doc = request.files.get('doc')
                cat = request.form["ddlcat"]
           
                if doc:
                    doc.save(os.path.join(".\webappfiles\static\images", doc.filename))
                    filepath = os.path.join("\static\images", doc.filename)
        
            
                updatep = "update tblproduct_advert set product_name =%s, descr =%s, document =%s,price=%s, cat_id =%s  where product_id = %s  "
                val = (name, desr, filepath,price,cat,s_id)
                cur.execute(updatep, val)
                con.commit()

                
                
                msg = str(cur.rowcount) + " record successfully updated"
                flash(msg, category='success')
                
              
                return redirect('/viewuseradvert/')
        except Exception as e:
                  msg = "Cannot be updated"
                  flash(msg, category='error')
              
            
        return render_template("updateproduct.html", rows=rows,rows1=rows1)
    else:
        return redirect('/login/')
    
    
    
        
@views.route("/homeadvert/", methods=["GET", "POST"])
def home_advert():
    current = datetime.now().date()
    view = "SELECT  s.s_id,s.service_name, s.descr, s.expiry_date, s.document, c.cat_type FROM tblservice_advert s JOIN tblcategory c ON s.cat_id = c.catid WHERE s.status = 'Approve' AND s.expiry_date >= %s"
    view1 = "SELECT p.product_id, p.product_name, p.descr, p.price, p.expiry_date, p.document, c.cat_type FROM tblproduct_advert p JOIN tblcategory c ON p.cat_id = c.catid WHERE p.status = 'Approve' AND p.expiry_date >= %s"
    val = (current,)
    
    
    cur.execute("SELECT * FROM tblcategory")
    categories = cur.fetchall()
    
    
    cur.execute("SELECT t.t_details, u.username FROM tbltestimonial t INNER JOIN tbluser u ON t.userid = u.id")
    testimonials = cur.fetchall()

    if request.method == 'POST':
        search = request.form['search']
        category = request.form['category']
        val1 = ('%' + search + '%',)

        if category == 'services':
            view += " AND s.service_name LIKE %s"
        elif category == 'products':
            view1 += " AND p.product_name LIKE %s"

        val += val1
        try:
            if category == 'services':
                cur.execute(view, val)
                rows = cur.fetchall()
                rows1 = []
            elif category == 'products':
                cur.execute(view1, val)
                rows1 = cur.fetchall()
                rows = []
        except Exception as e:
            print("Error occurred while fetching data:", str(e))
            rows = []
            rows1 = []

    else:
        try:
            cur.execute(view, val)
            rows = cur.fetchall()
        except Exception as e:
            print("Error occurred while fetching data:", str(e))
            rows = []

        try:
            cur.execute(view1, val)
            rows1 = cur.fetchall()
        except Exception as e:
            print("Error occurred while fetching data:", str(e))
            rows1 = []

    return render_template("mainhome.html", rows=rows, rows1=rows1,categories=categories,testimonials=testimonials)

@views.route("/category/<int:category_id>", methods=["GET"])
def view_category(category_id):
    try:
        current = datetime.now().date()
        cur.execute("SELECT * FROM tblcategory WHERE catid = %s", (category_id,))
        category = cur.fetchone()

        if not category:
            flash("Error: Category not found", category="error")
            return redirect('/homeadvert/')

        view = "SELECT s.s_id, s.service_name, s.descr, s.expiry_date, s.document, c.cat_type FROM tblservice_advert s JOIN tblcategory c ON s.cat_id = c.catid WHERE s.status = 'Approve' AND s.expiry_date >= %s AND s.cat_id = %s"
        view1 = "SELECT p.product_id, p.product_name, p.descr, p.price, p.expiry_date, p.document, c.cat_type FROM tblproduct_advert p JOIN tblcategory c ON p.cat_id = c.catid WHERE p.status = 'Approve' AND p.expiry_date >= %s AND p.cat_id = %s"
        val = (current, category_id)

        cur.execute(view, val)
        rows = cur.fetchall()
        
        cur.execute(view1, val)
        rows1 = cur.fetchall()

        return render_template("viewcat.html", category=category, rows=rows,rows1=rows1)

    except Exception as e:
        flash("Error: " + str(e), category="error")
        return redirect('/homeadvert/')

@views.route("/addtofavorites/", methods=["POST"])
def add_to_favorite():
     if "userid" in session:
         
        try:
            s_id = request.form["s_id"]
            id=session["userid"]
        
        
            finsert = "INSERT INTO tblfavourite_service (userid, s_id) VALUES (%s, %s)"
            
            values = (id, s_id) 

       
            cur.execute(finsert, values) 
            con.commit()
            flash("Item added to favorites", category="success")
        except Exception as e:
            con.rollback()  
            flash("Error occurred while adding to favorites." + str(e), category="error")
            print("Error:", e)
     else:
        flash("Please log in to add favorites.", category="error")
        
     return redirect(url_for("views.home_advert"))



@views.route("/addtofavorites1/", methods=["POST"])
def add_to_favorite1():
    if "userid" in session:
        
        try: 
            advert_id = request.form["p_id"]
            finsert = "INSERT INTO tblfavourite(id, p_id) VALUES (%s, %s)"
            values = (session["userid"], advert_id) 
                
            cur.execute(finsert, values) 
            con.commit()
            flash("Item added to favorites", category="success")
        except Exception as e:
            con.rollback()  
            flash("Error occurred while adding to favorites." + str(e), category="error")
            print("Error:", e)
    else:
        flash("Please log in to add favorites.", category="error")
        
    return redirect(url_for("views.home_advert"))




@views.route("/posttestimonial/", methods=['POST'])
def post_testimonial():
    if "userid" in session:
        id=session["userid"]
        
        if request.method=="POST":
            test=request.form.get("message")
            
            name="SELECT LNAME FROM tbluser where id=%s"
            val=(id,)
            cur.execute(name,val)
            row=cur.fetchone()[0]
            
            insert="INSERT INTO tbltestimonial(t_details,userid) VALUES(%s,%s)"
            val2=(test,id)
            cur.execute(insert,val2)
            con.commit()
            
            flash("Thank you for your support",category="success")
            
    return redirect('/about/')

@views.route("/make_offer/service", methods=['POST'])
def make_service_offer():
    if "userid" in session:
        amount = request.form.get("amount")
        message = request.form.get("message")
        advert_id = request.form.get("advert_id") 

        if advert_id and advert_id.isdigit():
            try:
                user = "SELECT lname, email, phone_number FROM tbluser WHERE id=%s"
                val2 = (session["userid"],)
                cur.execute(user, val2)
                rows2 = cur.fetchone()
                
                user1="SELECT email,lname from tbluser u  inner join tblservice_advert sa on sa.id =u.id where sa.s_id=%s"
                val4=(advert_id,)
                cur.execute(user1, val4)
                rows3= cur.fetchall()
                for em in rows3:
                    em=em[0]
                    ln=em[1]
    

                if not rows2:
                    flash("User not found.", category="error")
                    return redirect(url_for('home_advert'))

                lname =session.get("fn")
                email = rows2[1]
                phone_number = session.get("phone_number")
            
                insert = "INSERT INTO tbloffer_service (message, amount, s_id, userid) VALUES (%s, %s, %s, %s)"
                val = (message, amount, advert_id, session["userid"])
                cur.execute(insert, val)
                con.commit()
                flash("Offer for service submitted successfully.", category="success")
                
                
                msg = Message('PetiteAnnonce - New Offer Received', sender='darshanasramroop@gmail.com', recipients=[em])
                msg.body = f"Hello {ln},\n\nYou have received a new offer for your service advert.\n\nOffer Details:\nPlease log in to view the details\n"
                mail.send(msg)

            except Exception as e:
                con.rollback()
                flash("Error occurred: " + str(e), category="error")
        else:
            flash("Please enter a valid amount.", category="error")
    else:
        flash("Please log in.", category="error")

    return redirect(url_for('views.home_advert'))



@views.route("/make_offer/product", methods=['POST'])
def make_product_offer():
    if "userid" in session:
        amount = request.form.get("amount")
        message = request.form.get("message")
        advert_id = request.form.get("advert_id") 

        if advert_id and advert_id.isdigit():
            try:
        
                user = "SELECT lname, email, phone_number FROM tbluser WHERE id=%s"
                val2 = (session["userid"],)
                cur.execute(user, val2)
                rows2 = cur.fetchone()
                
                
                
                user1="SELECT email,lname from tbluser u  inner join tblproduct_advert sa on sa.id =u.id where sa.product_id=%s"
                val4=(advert_id,)
                cur.execute(user1, val4)
                rows3= cur.fetchall()
                for em in rows3:
                    em=em[0]
                    ln=em[1]

                if not rows2:
                    flash("User not found.", category="error")
                    return redirect(url_for('home_advert'))


               
                lname =session.get("fn")
                email = rows2[1]
                phone_number = session.get("phone_number")
            
            
                insert = "INSERT INTO tbloffer (message, amount, product_id, userid) VALUES (%s, %s, %s, %s)"
                val = (message, amount, advert_id, session["userid"])
                cur.execute(insert, val)
                con.commit()
                flash("Offer for product submitted successfully.", category="success")
                
                
                 
                msg = Message('PetiteAnnonce - New Offer Received', sender='darshanasramroop@gmail.com', recipients=[em])
                msg.body = f"Hello {ln},\n\nYou have received a new offer for your product advert.\n\nOffer Details:\nPlease log in to view the details\n"
                mail.send(msg)

            except Exception as e:
                con.rollback()
                flash("Error occurred: " + str(e), category="error")
        else:
            flash("Please enter a valid amount.", category="error")
    else:
        flash("Please log in.", category="error")

    return redirect(url_for('views.home_advert'))

    
@views.route("/viewexpireduseradvert/", methods=['GET', 'POST'])
def view_exuseradvert():
    rows = [] 
    rows1=[]
    if 'userid' in session:
        id=session.get('userid')
        
        current = datetime.now().date()
        exp = current - timedelta(days=7)
        
        view="select * from tblservice_advert pa inner join tbluser u on pa.id=u.id INNER JOIN tblcategory AS c ON pa.cat_id = c.catid where u.id=%s and pa.expiry_date < %s and pa.request=0 "
        val=(id,current)
        cur.execute(view,val)
        rows = cur.fetchall()
        
        
        pview = "SELECT * FROM tblproduct_advert pa INNER JOIN tbluser u ON pa.id = u.id INNER JOIN tblcategory AS c ON pa.cat_id = c.catid WHERE u.id = %s and pa.expiry_date< %s  and pa.request=0"
        cur.execute(pview, val)
        rows1 = cur.fetchall()
        
                
             
    return render_template("Expiredadvert.html",rows=rows,rows1=rows1)



    
     
@views.route("/renewproduct/")
def pro_new():
    if 'userid' in session:
        s_id = request.args.get('productid') 
        user_id = session.get('userid')
        sql = "SELECT * FROM tblproduct_advert WHERE product_id = %s AND id = %s"
        val = (s_id,user_id )
        cur.execute(sql, val)
        rows = cur.fetchall()
    return render_template('renew.html', rows=rows)
    
    
@views.route("/renew/", methods=["GET", "POST"])
def reneww():
    if 'userid' in session:
        user_id = session.get('userid')
        s_id = request.form.get('productid')
        rows=None
       
        sql = "SELECT * FROM tblproduct_advert WHERE product_id = %s "
        val = (s_id,)
        cur.execute(sql, val)
        rows = cur.fetchall()
            
        try:
              
           
                
            if request.method == "POST":
            
                
            
                updatep = "update tblproduct_advert set request =%s where product_id = %s AND id = %s  "
                val = (1,s_id,user_id)
                cur.execute(updatep, val)
                con.commit()

                
                
                msg = str(cur.rowcount) + " record successfully updated"
                flash(msg, category='success')
                
              
                return redirect('/viewexpireduseradvert/')
        except:
                msg = "Cannot be updated"
                flash(msg, category='error')
              
            
        return render_template("renew.html", rows=rows)
    else:
        return redirect('/login/')
    


    
@views.route("/renewsservice/")
def pro_neww():
    if 'userid' in session:
        s_id = request.args.get('productid') 
        user_id = session.get('userid')
        sql = "SELECT * FROM tblservice_advert WHERE s_id = %s AND id = %s"
        val = (s_id,user_id )
        cur.execute(sql, val)
        rows = cur.fetchall()
    return render_template('renew1.html', rows=rows)
    
    
@views.route("/reneww/", methods=["GET", "POST"])
def renewww():
    if 'userid' in session:
        user_id = session.get('userid')
        s_id = request.form.get('productid')
        rows=None
       
        sql = "SELECT * FROM tblservice_advert WHERE s_id = %s "
        val = (s_id,)
        cur.execute(sql, val)
        rows = cur.fetchall()
            
        try:
              
           
                
            if request.method == "POST":
            
                
            
                updatep = "update tblservice_advert set request =%s where s_id = %s AND id = %s  "
                val = (1,s_id,user_id)
                cur.execute(updatep, val)
                con.commit()

                
                
                msg = str(cur.rowcount) + " record successfully updated"
                flash(msg, category='success')
                
              
                return redirect('/viewexpireduseradvert/')
        except:
                msg = "Cannot be updated"
                flash(msg, category='error')
              
            
        return render_template("renew.html", rows=rows)
    else:
        return redirect('/login/')
    
    
@views.route("/viewfavorite/", methods=['GET', 'POST'])   
def view_faavourite():
    rows = []
    rows1 = []

    if 'userid' in session:
        user_id = session.get('userid')
        current = datetime.now().date()

   
      
        view1 = "SELECT * FROM  tblfavourite_service sf INNER JOIN tblservice_advert sa ON sf.s_id = sa.s_id INNER JOIN tblcategory AS c ON sa.cat_id = c.catid WHERE sf.userid = %s AND sa.expiry_date >= %s"
        val = (user_id, current)
        cur.execute(view1, val)
        rows = cur.fetchall()

        
        view = "SELECT * FROM tblfavourite f INNER JOIN tblproduct_advert pa ON f.p_id = pa.product_id INNER JOIN tblcategory AS c ON pa.cat_id = c.catid  WHERE f.id = %s AND pa.expiry_date >= %s"
        val1 = (user_id, current)
        cur.execute(view, val1)
        rows1 = cur.fetchall()

    return render_template("viewfavouite.html",rows=rows,rows1=rows1)

 
   

