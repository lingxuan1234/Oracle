create table car(
       id number(7) primary key,
       brand varchar2(50),
       model varchar2(50),
       price varchar2(50),
       fld varchar2(50) 
);

create sequence car_seq
minvalue 1
maxvalue 9999999999999
start with 1
increment by 1
nocycle
nocache
order;

create or replace trigger car_tri
  before insert on car
  for each row
declare
   nextid number;
begin
  if :new.id is null or :new.id = 0 then
    select car_seq.nextval into nextid from dual;
    :new.id := nextid;
  end if;
end;

create table firm(
       id varchar2(50) primary key,
       name varchar2(50),
       domestic varchar2(50),
       summary varchar2(50)
);


create sequence firm_seq
minvalue 1
maxvalue 9999999999999
start with 1
increment by 1
nocycle
nocache
order;

create or replace trigger firm_tri
  before insert on firm
  for each row
declare
   nextid number;
begin
  if :new.id is null or :new.id = 0 then
    select firm_seq.nextval into nextid from dual;
    :new.id := nextid;
  end if;
end;


alter table car
   add constraint fk_fld_car_firm foreign key (fld)
      references firm(id); 
         




