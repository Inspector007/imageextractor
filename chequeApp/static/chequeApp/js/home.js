/**
 * Created by root on 3/9/16.
 */
    function text(imageid) {
        id = document.getElementById('loginid').value;
        //alert(id+"------------------");
        // document.getElementById("btnConvert").disabled = true;
        //document.getElementById('loadImage').disabled = false;
        // Get the modal
    var modal = document.getElementById('myModal');
        modal.style.display = 'block';

        $.ajax({
            type :'POST',
            //dataType: 'json',
            //contentType: 'application/json; charset=utf-8',
            url: '/converter/returntext/',
            data: {'imgid': imageid,'loginid' : id},
            //dataType: 'text',
            //processData: false,
            success: function(data) {
                modal.style.display = 'none';
          //      alert(data);
            if(imageid == '')
            {
                $("#imageText").html(data);
            }
            if(imageid == '1')
            {
                $("#imageText1").html(data);
            }
            if(imageid == '2')
            {
                $("#imageText2").html(data);
            }

            },
            failure: function(data) {
            alert('Got an error');
            }
        });
        //alert(" EXTRACTING.....");
    }

function text1(fileObj) {
        id = document.getElementById('loginid').value;
        x1 = document.getElementById('x1').value;
        y1 = document.getElementById('y1').value;
        x2 = document.getElementById('x2').value;
        y2 = document.getElementById('y2').value;
        // alert(x1+"--"+y1+"--"+x2+"--"+y2);

        //alert(id);
        var modal = document.getElementById('myModal');
        modal.style.display = 'block';
      

        $.ajax({
            type :'POST',
            url: '/converter/returntextAC/',
            data: {'loginid' : id},
            //data: fileObj,
            //dataType: JSON,
            //processData: false,
            dataType: 'json',
            contentType: 'application/json; charset=utf-8',
            //type: 'POST',
            success: function(data) {
               // alert(typeof data);
                modal.style.display = 'none';
                $("#accountnumber").val(data[0]);
                $("#ifsccode").val(data[1]);
                $("#imageText").html(data[2]);
            },
            failure: function(data) {
            alert('Got an error');
            }
        });
    }




function textCrop(fileObj) {
        id = document.getElementById('loginid').value;
        x1 = document.getElementById('x1').value;
        y1 = document.getElementById('y1').value;
        x2 = document.getElementById('x2').value;
        y2 = document.getElementById('y2').value;
        //alert(x1+"--"+y1+"--"+x2+"--"+y2);

        // alert('textCrop'+id);
        var modal = document.getElementById('myModal');
        modal.style.display = 'block';
    
        $.ajax({
            type :'POST',
            url: '/converter/returntextCrop/',
            data: {'loginid' : id},
            //data: fileObj,
            //dataType: JSON,
            //processData: false,
            dataType: 'json',
            contentType: 'application/json; charset=utf-8',
            //type: 'POST',
            success: function(data) {
               // alert(typeof data);
                modal.style.display = 'none';
            $("#accountnumber").val(data[0]);
                $("#ifsccode").val(data[1]);
                $("#imageText").html(data[2]);
            },
            failure: function(data) {
            alert('Got an error');
            }
        });
    }

function textCropAjax(cropValue,imageid) {
        id = document.getElementById('cropid').value;
        // id1 = document.getElementById('loginid').value;

        // alert("TExtCrop Ajax"+cropValue);
        console.log("imageid"+imageid+"id cropvalue"+id)
        x1 = document.getElementById('x1').value;
        y1 = document.getElementById('y1').value;
        x2 = document.getElementById('x2').value;
        y2 = document.getElementById('y2').value;
        // alert(x1+"--"+y1+"--"+x2+"--"+y2);

        var modal = document.getElementById('myModal');
        modal.style.display = 'block';
        // alert(id);

        $.ajax({
            type :'POST',
            url: '/converter/selectimagetestNewAjax/',
            data: {'imgid':imageid,'cropid':id,'x1':x1,'y1':y1,'x2':x2,'y2':y2},
            //data: fileObj,
            //dataType: JSON,
            //processData: false,
            // dataType: 'json',
            // contentType: 'application/json; charset=utf-8',
            //type: 'POST',
            success: function(data) {
               // alert(typeof data);
               //  modal.style.display = 'none';
               //  alert("hellosdhfsfkshdfhsdfhkshdfh");
                // location.reload();
            // $("#accountnumber").val(data[0]);
            //     $("#ifsccode").val(data[1]);
            //     $("#imageText").html(data[2]);

        $.ajax({
            type :'POST',
            url: '/converter/returnmutualcroptext/',
            data: {'imgid':imageid,'loginid' : id},
            //data: fileObj,
            //dataType: JSON,
            //processData: false,
            dataType: 'json',
            contentType: 'application/json; charset=utf-8',
            //type: 'POST',
            success: function(data) {
               // alert(typeof data);
    //            alert(data[2]);
                modal.style.display = 'none';
                if(cropValue == '21')
                    {
                    var str1 = data[2];
                    alert("data2"+data[2]);
                    var re = /([A-Za-z]{0,2}[0-9]{3,9})/;
                    var found = str1.match(re);
                    alert("found"+found[0]);
                    if(found.length >= 1)
                        $("#mdpid").val(found[0]);
                    else
                        $("#mdpid").val(data[2]);
                }
                 //   $("#mdpid").val(data[2]);
                if(cropValue == '22') {
                    var str1 = data[2];
                    //alert("data2"+data[2]);
                    var re = /([0-9]{1,2}[-]{0,1}[A-Za-z]{2,3}[-]{0,1}[0-9]{2,4})/;
                    var found = str1.match(re);
                    //alert("found"+found[0]);
                    if(found.length >= 1)
                        $("#mudate").val(found[0]);
                    else
                        $("#mudate").val(data[2]);
                }
                if(cropValue == '23')
                    $("#misin").val(data[2]);
                if(cropValue == '24')
                    $("#munits").val(data[2]);
                /*if(cropValue == '25')
                    $("#mfolio").val(data[2]);
                if(cropValue == '26')
                    $("#maverageprice").val(data[2]);*/

                if(cropValue == '27')
                    $("#mfdpid").val(data[2]);
                if(cropValue == '28')
                    $("#mfudate").val(data[2]);
                if(cropValue == '29')
                    $("#mfisin").val(data[2]);
                if(cropValue == '30')
                    $("#mfunits").val(data[2]);
                if(cropValue == '31')
                    $("#mffolio").val(data[2]);
                if(cropValue == '32')
                    $("#mfaverageprice").val(data[2]);

                if(cropValue == '33')
                {
                    var str1 = data[2];
                    alert("data2"+data[2]);
                    var re = /([A-Za-z]{0,2}[0-9]{3,9})/;
                    var found = str1.match(re);
                    alert("found"+found[0]);
                    if(found.length >= 1)
                        $("#mdpid").val(found[0]);
                    else
                        $("#mdpid").val(data[2]);
                }
                if(cropValue == '34')
                    $("#eudate").val(data[2]);
                if(cropValue == '35')
                    $("#eisin").val(data[2]);
                if(cropValue == '36')
                    $("#eunits").val(data[2]);
                if(cropValue == '37')
                    $("#efolio").val(data[2]);
                if(cropValue == '38')
                    $("#eaverageprice").val(data[2]);


                if(cropValue == '1')
                    $("#accountnumber").val(data[2]);
                if(cropValue == '2')
                    $("#ifsccode").val(data[2]);
                if(cropValue == '3'){
                    $("#acholder").val(data[2]);
                    // $("#imageText").html(data[2]);
                    }
                if(cropValue == '4'){
                    $("#cropText").val(data[2]);
                    // $("#imageText").html(data[2]);
                    }
                if(cropValue == '5'){
                    //$("#address").val(data[2]);
                    $("#city").val(data[0]);
                    $("#state").val(data[1]);
                    $("#imageText1").val(data[2]);
                    $("#zipcode").val(data[3]);
                    // $("#imageText").html(data[2]);
                    }
                                if(cropValue == '6'){
                    $("#city").val(data[2]);
                    // $("#imageText").html(data[2]);
                    }
                                if(cropValue == '7'){
                    $("#state").val(data[2]);
                    // $("#imageText").html(data[2]);
                    }
                                if(cropValue == '8'){
                    $("#zipcode").val(data[2]);
                    // $("#imageText").html(data[2]);
                    }
                                if(cropValue == '9'){
                    // $("#address1").val(data[2]);
                    $("#city1").val(data[0]);
                    $("#state1").val(data[1]);
                    $("#imageText2").val(data[2]);
                    $("#zipcode1").val(data[3]);
                    // $("#imageText").html(data[2]);
                    }
                                if(cropValue == '10'){
                    $("#city1").val(data[2]);
                    // $("#imageText").html(data[2]);
                    }
                                if(cropValue == '11'){
                    $("#state1").val(data[2]);
                    // $("#imageText").html(data[2]);
                    }
                                if(cropValue == '12'){
                    $("#zipcode1").val(data[2]);
                    // $("#imageText").html(data[2]);
                    }
            },
            failure: function(data) {
            alert('Got an error');
            }
        });
            },
            failure: function(data) {
            alert('Got an error');
            }
        });
    // location.reload();
    }

function textCropAjaxMutualEquity(cropValue,imageid) {
        // alert("textCropAjaxMutualEquity");
        // var id = document.getElementById('msg1').value;
        id = document.getElementById('cropid').value;
        // alert(id);

        // id1 = document.getElementById('loginid').value;
        var count1 = document.getElementById('rowcount1').value;
        var count2 = document.getElementById('rowcount2').value;
        var count3 = document.getElementById('rowcount3').value;

        //alert("TExtCrop Ajax"+cropValue);
        x1 = document.getElementById('x1').value;
        y1 = document.getElementById('y1').value;
        x2 = document.getElementById('x2').value;
        y2 = document.getElementById('y2').value;
        // alert(x1+"--"+y1+"--"+x2+"--"+y2);
        var modal = document.getElementById('myModal');
        modal.style.display = 'block';
        // alert(id);

        $.ajax({
            type :'POST',
            url: '/converter/selectimagetestNewAjax/',
            data: {'imgid':imageid,'cropid':id,'x1':x1,'y1':y1,'x2':x2,'y2':y2},
            //data: fileObj,
            //dataType: JSON,
            //processData: false,
            // dataType: 'json',
            // contentType: 'application/json; charset=utf-8',
            //type: 'POST',
            success: function(data) {
               // alert(typeof data);
               //  modal.style.display = 'none';
               //  alert("hellosdhfsfkshdfhsdfhkshdfh");
                // location.reload();
            // $("#accountnumber").val(data[0]);
            //     $("#ifsccode").val(data[1]);
            //     $("#imageText").html(data[2]);

        $.ajax({
            type :'POST',
            url: '/converter/returnmutualcroptext/',
            data: {'imgid':imageid,'loginid' : id,'cropvalue':cropValue},
            //data: fileObj,
            //dataType: JSON,
            //processData: false,
            dataType: 'json',
            contentType: 'application/json; charset=utf-8',
            //type: 'POST',
            success: function(data) {
               // alert(typeof data);
    //            alert(data[2]);

                modal.style.display = 'none';
                if(cropValue == '21')
                    {

                        $("#mdpid").val(data[0]);
                }
                 //   $("#mdpid").val(data[2]);
                if(cropValue == '22') {
                        $("#mudate").val(data[0]);
                }

                if(cropValue == '23') {
                    // alert("data"+count1+"----"+data.length);
                    if(data.length > count1 && count1 == "")
                    {
                        // alert("data if"+count1+"----"+data.length);
                        $("#rowcount1").val(data.length);

                    $.each(data,function (i,objvalue) {
                        // alert(objvalue);
                        $("#cropDiv13").append(
                        $("<input/>", {
                        type: 'text',
                        id: "misin"+i,
                        name: "misin"+i,
                        value: objvalue
                        }),$("<br/>"));

                    });
                        $("#btnmisin").attr('disabled',true);
                        $("#btnmunits").attr('disabled',false);
                    }

                   // condition 2
                   if((data.length >= count1 && count1 != "") || (data.length <= count1 && count1 != ""))
                    {
                        // alert("data if con 2"+count1+"----"+data.length);
                        $("#rowcount1").val(data.length+parseInt(count1));
                        x = parseInt(count1);
                    $.each(data,function (i,objvalue) {
                        // alert(objvalue);
                        $("#cropDiv13").append(
                        $("<input/>", {
                        type: 'text',
                        id: "misin"+(x),
                        name: "misin"+(x++),
                        value: objvalue
                        }),$("<br/>"));

                    });
                        $("#btnmisin").attr('disabled',true);
                        $("#btnmunits").attr('disabled',false);
                    }

                }
                if(cropValue == '24')
                {
                    // alert(data.length);

                    // alert("data"+count1+"----"+data.length);
                    if(data.length < parseInt(count1))
                    {
                        var t = parseInt(count1)-data.length;
                        alert("data if"+count1+"----"+data.length+"--");
                        // $("#rowcount1").val(data.length);
                        for(var p=0;p<t;p++)
                        {
                            alert(p);
                            data.push("");
                        }
                        $.each(data,function (i,objvalue) {
                        // alert(objvalue);
                        $("#cropDiv14").append(
                        $("<input/>", {
                        type: 'text',
                        id: "munits"+i,
                        name: "munits"+i,
                        value: objvalue
                        }),$("<br/>"));

                    });
                        $("#btnmisin").attr('disabled',true);
                        $("#btnmunits").attr('disabled',true);

                    }
                    else
                    {
                        // alert(data.length+"---"+parseInt(count1));
                        var t1 = [];
                        for(var p=0;p<parseInt(count1);p++)
                        {
                            t1[p] = data[p];
                            // alert(t[p]+"--"+data[p]);
                        }
                        // alert(t.length);

                        $.each(t1,function (i,objvalue) {
                        // alert(objvalue);
                        $("#cropDiv14").append(
                        $("<input/>", {
                        type: 'text',
                        id: "munits"+i,
                        name: "munits"+i,
                        value: objvalue
                        }),$("<br/>"));

                    });
                        $("#btnmisin").attr('disabled',true);
                        $("#btnmunits").attr('disabled',true);

                    }

                    // $("#munits").val(data);

                }

                /*if(cropValue == '25')
                    $("#mfolio").val(data[2]);
                if(cropValue == '26')
                    $("#maverageprice").val(data[2]);*/

                if(cropValue == '27')
                    $("#mfdpid").val(data[2]);
                if(cropValue == '28')
                    $("#mfudate").val(data[2]);
                if(cropValue == '29')
                {
                    // alert("data"+count2+"----"+data.length);
                    if(data.length > count2 && count2 == "")
                    {
                        // alert("data if"+count1+"----"+data.length);
                        $("#rowcount2").val(data.length);

                    $.each(data,function (i,objvalue) {
                        // alert(objvalue);
                        $("#cropDiv22").append(
                        $("<input/>", {
                        type: 'text',
                        id: "mfisin"+i,
                        name: "mfisin"+i,
                        value: objvalue
                        }),$("<br/>"));

                    });
                        $("#btnmfisin").attr('disabled',true);
                        $("#btnmffolio").attr('disabled',false);

                    }

                   // condition 2
                   if((data.length >= count2 && count2 != "") || (data.length <= count2 && count2 != ""))
                    {
                        // alert("data if con 2"+count1+"----"+data.length);
                        $("#rowcount2").val(data.length+parseInt(count2));
                        x = parseInt(count2);
                    $.each(data,function (i,objvalue) {
                        // alert(objvalue);
                        $("#cropDiv22").append(
                        $("<input/>", {
                        type: 'text',
                        id: "mfisin"+(x),
                        name: "mfisin"+(x++),
                        value: objvalue
                        }),$("<br/>"));

                    });
                        $("#btnmfisin").attr('disabled',true);
                        $("#btnmffolio").attr('disabled',false);
                    }
                }

                if(cropValue == '30')
                {
                    // alert(data.length);
                    // $("#mfunits").val(data);

                    // alert("data"+count2+"----"+data.length);
                    if(data.length < parseInt(count2))
                    {
                        var t = parseInt(count2)-data.length;
                        // alert("data if"+count2+"----"+data.length+"--");
                        // $("#rowcount1").val(data.length);
                        for(var p=0;p<t;p++)
                        {
                            // alert(p);
                            data.push("");
                        }
                        $.each(data,function (i,objvalue) {
                        // alert(objvalue);
                        $("#cropDiv24").append(
                        $("<input/>", {
                        type: 'text',
                        id: "mfunits"+i,
                        name: "mfunits"+i,
                        value: objvalue
                        }),$("<br/>"));

                    });
                        $("#btnmfavereageprice").attr('disabled',false);
                        $("#btnmfunits").attr('disabled',true);
                    }
                    else
                    {
                        var t1 = [];
                        for(var p=0;p<parseInt(count2);p++)
                        {
                            t1[p] = data[p];
                            // alert(t[p]+"--"+data[p]);
                        }
                        $.each(t1,function (i,objvalue) {
                        // alert(objvalue);
                        $("#cropDiv24").append(
                        $("<input/>", {
                        type: 'text',
                        id: "mfunits"+i,
                        name: "mfunits"+i,
                        value: objvalue
                        }),$("<br/>"));

                    });
                        $("#btnmfavereageprice").attr('disabled',false);
                        $("#btnmfunits").attr('disabled',true);
                    }
                }

                if(cropValue == '31')
                {
                    // alert(data.length);
                    // $("#mffolio").val(data);
                    // alert("data"+count2+"----"+data.length);
                    if(data.length < parseInt(count2))
                    {
                        var t = parseInt(count2)-data.length;
                        // alert("data if"+count2+"----"+data.length+"--");
                        // $("#rowcount1").val(data.length);
                        for(var p=0;p<t;p++)
                        {
                            // alert(p);
                            data.push("");
                        }
                        $.each(data,function (i,objvalue) {
                        // alert(objvalue);
                        $("#cropDiv23").append(
                        $("<input/>", {
                        type: 'text',
                        id: "mffolio"+i,
                        name: "mffolio"+i,
                        value: objvalue
                        }),$("<br/>"));

                    });
                        $("#btnmffolio").attr('disabled',true);
                        $("#btnmfunits").attr('disabled',false);
                    }
                    else
                    {
                        var t1= [];
                        for(var p=0;p<parseInt(count2);p++)
                        {
                            t1[p] = data[p];
                            // alert(t1[p]+"--"+data[p]);
                        }

                        $.each(t1,function (i,objvalue) {
                        // alert(objvalue);
                        $("#cropDiv23").append(
                        $("<input/>", {
                        type: 'text',
                        id: "mffolio"+i,
                        name: "mffolio"+i,
                        value: objvalue
                        }),$("<br/>"));

                    });
                        $("#btnmffolio").attr('disabled',true);
                        $("#btnmfunits").attr('disabled',false);
                    }

                }

                if(cropValue == '32')
                {
                    // $("#mfaverageprice").val(data);
                    // alert("data"+count2+"----"+data.length);
                    if(data.length < parseInt(count2))
                    {
                        var t = parseInt(count2)-data.length;
                        // alert("data if"+count2+"----"+data.length+"--");
                        // $("#rowcount1").val(data.length);
                        for(var p=0;p<t;p++)
                        {
                            // alert(p);
                            data.push("");
                        }
                        $.each(data,function (i,objvalue) {
                        // alert(objvalue);
                        $("#cropDiv25").append(
                        $("<input/>", {
                        type: 'text',
                        id: "mfaverageprice"+i,
                        name: "mfaverageprice"+i,
                        value: objvalue
                        }),$("<br/>"));
                    });
                        $("#btnmfavereageprice").attr('disabled',true);
                    }
                    else
                    {
                        var t1 = [];
                        for(var p=0;p<parseInt(count2);p++)
                        {
                            t1[p] = data[p];
                            // alert(t1[p]+"--"+data[p]);
                        }

                        $.each(t1,function (i,objvalue) {
                        // alert(objvalue);
                        $("#cropDiv25").append(
                        $("<input/>", {
                        type: 'text',
                        id: "mfaverageprice"+i,
                        name: "mfaverageprice"+i,
                        value: objvalue
                        }),$("<br/>"));
                    });
                        $("#btnmfavereageprice").attr('disabled',true);
                    }

                }

                if(cropValue == '33')
                {
                        $("#edpid").val(data[0]);
                }
                if(cropValue == '34')
                    $("#eudate").val(data[2]);

                if(cropValue == '35')
                {
                    // alert("data"+count3+"----"+data.length);
                    if(data.length > count3 && count3 == "")
                    {
                        // alert("data if"+count3+"----"+data.length);
                        $("#rowcount3").val(data.length);

                    $.each(data,function (i,objvalue) {
                        // alert(objvalue);
                        $("#cropDiv33").append(
                        $("<input/>", {
                        type: 'text',
                        id: "eisin"+i,
                        name: "eisin"+i,
                        value: objvalue
                        }),$("<br/>"));

                    });
                        $("#btneisin").attr('disabled',true);
                        $("#btneshares").attr('disabled',false);
                    }

                   // condition 2
                   if((data.length >= count3 && count3 != "") || (data.length <= count3 && count3 != ""))
                    {
                        // alert("data if con 2"+count3+"----"+data.length);
                        $("#rowcount3").val(data.length+parseInt(count3));
                        x = parseInt(count3);
                    $.each(data,function (i,objvalue) {
                        // alert(objvalue);
                        $("#cropDiv33").append(
                        $("<input/>", {
                        type: 'text',
                        id: "eisin"+(x),
                        name: "eisin"+(x++),
                        value: objvalue
                        }),$("<br/>"));

                    });
                        $("#btneisin").attr('disabled',true);
                        $("#btneshares").attr('disabled',false);
                    }
                }

                if(cropValue == '36')
                {
                    // alert("data"+count3+"----"+data.length);
                    if(data.length < parseInt(count3))
                    {
                        var t = parseInt(count3)-data.length;
                        // alert("data if"+count3+"----"+data.length+"--");
                        // $("#rowcount1").val(data.length);
                        for(var p=0;p<t;p++)
                        {
                            // alert(p);
                            data.push("");
                        }
                        $.each(data,function (i,objvalue) {
                        // alert(objvalue);
                        $("#cropDiv34").append(
                        $("<input/>", {
                        type: 'text',
                        id: "eunits"+i,
                        name: "eunits"+i,
                        value: objvalue
                        }),$("<br/>"));

                    });
                        $("#btneshares").attr('disabled',true);
                        $("#btneaverageprice").attr('disabled',false);
                    }
                    else
                    {
                        var t1 = [];
                        for(var p=0;p<parseInt(count3);p++)
                        {
                            t1[p] = data[p];
                            // alert(t[p]+"--"+data[p]);
                        }
                        $.each(t1,function (i,objvalue) {
                        // alert(objvalue);
                        $("#cropDiv34").append(
                        $("<input/>", {
                        type: 'text',
                        id: "eunits"+i,
                        name: "eunits"+i,
                        value: objvalue
                        }),$("<br/>"));

                    });
                        $("#btneshares").attr('disabled',true);
                        $("#btneaverageprice").attr('disabled',false);
                    }

                }

                if(cropValue == '37')
                {
                    alert(data.length);
                    // $("#efolio").val(data);
                }

                if(cropValue == '38')
                {
                    // alert("data"+count3+"----"+data.length);
                    if(data.length < parseInt(count3))
                    {
                        var t = parseInt(count3)-data.length;
                        // alert("data if"+count3+"----"+data.length+"--");
                        // $("#rowcount1").val(data.length);
                        for(var p=0;p<t;p++)
                        {
                            // alert(p);
                            data.push("");
                        }
                        $.each(data,function (i,objvalue) {
                        // alert(objvalue);
                        $("#cropDiv35").append(
                        $("<input/>", {
                        type: 'text',
                        id: "eaverageprice"+i,
                        name: "eaverageprice"+i,
                        value: objvalue
                        }),$("<br/>"));

                    });
                        $("#btneaverageprice").attr('disabled',true);

                    }
                    else
                    {
                        var t1 = [];
                        for(var p=0;p<parseInt(count3);p++)
                        {
                            t1[p] = data[p];
                            // alert(t[p]+"--"+data[p]);
                        }
                        $.each(t1,function (i,objvalue) {
                        // alert(objvalue);
                        $("#cropDiv35").append(
                        $("<input/>", {
                        type: 'text',
                        id: "eaverageprice"+i,
                        name: "eaverageprice"+i,
                        value: objvalue
                        }),$("<br/>"));

                    });
                        $("#btneaverageprice").attr('disabled',true);
                    }
                }

                
            },
            failure: function(data) {
            alert('Got an error');
            }
        });
            },
            failure: function(data) {
            alert('Got an error');
            }
        });
    // location.reload();
    }

function setCookie(cname,cvalue,exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    var expires = "expires=" + d.toGMTString();
    document.cookie = cname+"="+cvalue+"; "+expires;
}

function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i=0; i<ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}
function checkCookie() {
    var user=getCookie("username");
    //document.getElementById('convertCrop').disabled = true;
    if (user != "") {
        // alert("Welcome again " + user);
        document.getElementById('loginid').value = user;
        document.getElementById('cropid').value = user;
    } else {
       user = prompt("Please enter Your Employee ID:","");
       if (user != "" && user != null) {
           setCookie("username", user, 30);
           document.getElementById('loginid').value = user;
       }
    }
}

function btnDisable() {
    document.getElementById('convert').disabled = true;
    document.getElementById('convertCrop').disabled = false;
}

function hello() {
    var file_data = $('#images').prop('files')[0];
    var loginid = document.getElementById('loginid').value;
    var form_data = new FormData();
    form_data.append('file', file_data);
    form_data.append('loginId',loginid);
    alert(form_data);

    $.ajax({
    type: "POST",
    url: "/converter/home/",
    data: form_data,
    processData: false,  // tell jQuery not to process the data
    contentType: false   // tell jQuery not to set contentType
});

}

function mysubmit() {
    document.getElementById("myForm").submit();
}

function showdetail() {
    clientid = document.getElementById('clientid').value;
    // alert("lasjd"+clientid);
            $.ajax({
        type: "POST",
        url :"/converter/showclient/",
        data: {'clientid':clientid},
        dataType: 'json',
        contentType: 'application/json; charset=utf-8',
        success: function (data) {
            if(clientid == data[0]) {
                // alert(data)
                document.getElementById('cid').value = data[0]
                document.getElementById('cname').value = data[1]
                document.getElementById('caddress').value = data[2]
                document.getElementById('cac').value = data[3]
                document.getElementById('cpan').value = data[4]
                document.getElementById('caadhar').value = data[5]
                document.getElementById('cifsc').value = data[6]
                document.getElementById('cbank').value = data[7]
            }
            else{
                document.getElementById('cid').value = ""
                document.getElementById('cname').value = ""
                // document.getElementById('caddress').value = data[2]
                // document.getElementById('cac').value = data[3]
                document.getElementById('cpan').value = ""
                // document.getElementById('caadhar').value = data[5]
                // document.getElementById('cifsc').value = data[6]
                // document.getElementById('cbank').value = data[7]
                document.getElementById('msg').value = ""
                alert(data)
            }
        },
        failure:function (data) {
            alert("error during db operation")
        }
    })

}

function updatebankdetail() {
    clientid = document.getElementById('clientid').value;
    acno = document.getElementById('accountnumber').value;
    ifscno = document.getElementById('ifsccode').value;
    acholder = document.getElementById('acholder').value;

    $.ajax({
        type: "POST",
        url :"/converter/updateclient/",
        data: {'clientid':clientid,'acno':acno,'ifscno':ifscno,'acholder':acholder},
        dataType: 'json',
        contentType: 'application/json; charset=utf-8',
        success:function (data) {
            alert(data);
        },
        failure:function (data) {
            alert("Error"+data);
        }
    })
}

function cleardetail() {
    document.getElementById('cid').value = ""
                document.getElementById('cname').value = ""
                document.getElementById('caddress').value = ""
                document.getElementById('cac').value = ""
                document.getElementById('cpan').value = ""
                document.getElementById('caadhar').value = ""
                document.getElementById('cifsc').value = ""
                document.getElementById('cbank').value = ""
                document.getElementById('accountnumber').value = ""
                document.getElementById('acholder').value = ""
                document.getElementById('ifsccode').value = ""
                document.getElementById('imageText').value = ""
                document.getElementById('address11').value = ""
                document.getElementById('address12').value = ""
                document.getElementById('address13').value = ""
                document.getElementById('city').value = ""
                document.getElementById('state').value = ""
                document.getElementById('zipcode').value = ""
                document.getElementById('imageText1').value = ""
                document.getElementById('address21').value = ""
                document.getElementById('address22').value = ""
                document.getElementById('address23').value = ""
                document.getElementById('city1').value = ""
                document.getElementById('state1').value = ""
                document.getElementById('zipcode1').value = ""
                document.getElementById('imageText2').value = ""
}

function menuclear() {
    document.getElementById('accountnumber').value = ""
    document.getElementById('acholder').value = ""
    document.getElementById('ifsccode').value = ""
    document.getElementById('imageText').value = ""
}

function menu1clear() {
                document.getElementById('address11').value = ""
                document.getElementById('address12').value = ""
                document.getElementById('address13').value = ""
                document.getElementById('city').value = ""
                document.getElementById('state').value = ""
                document.getElementById('zipcode').value = ""
                document.getElementById('imageText1').value = ""
}

function menu2clear() {
                document.getElementById('address21').value = ""
                document.getElementById('address22').value = ""
                document.getElementById('address23').value = ""
                document.getElementById('city1').value = ""
                document.getElementById('state1').value = ""
                document.getElementById('zipcode1').value = ""
                document.getElementById('imageText2').value = ""
}


function inmutualM()
{
    // //alert("inmutual");
    // document.getElementById('mdpid').value = "";
    // document.getElementById('misin').value = "";
    // document.getElementById('munits').value = "";
    // alert(document.getElementById('rowcount1').value);
    $('#cropDiv13').find('br').remove();
    $('#cropDiv14').find('br').remove();
    $("#btnmisin").attr('disabled',false);
    for(var i=0;i<document.getElementById('rowcount1').value;i++)
    {
        document.getElementById('cropDiv13').removeChild(document.getElementById('misin'+i));
        if(document.getElementById('munits'+i))
            document.getElementById('cropDiv14').removeChild(document.getElementById('munits'+i));
    }
    document.getElementById('rowcount1').value = "";

}

function inmutualF()
{
    // alert("inmutual");
    // document.getElementById('mffolio').value = "";
    // document.getElementById('mfisin').value = "";
    // document.getElementById('mfunits').value = "";
    // document.getElementById('mfaverageprice').value = "";
    $('#cropDiv22').find('br').remove();
    $('#cropDiv23').find('br').remove();
    $('#cropDiv24').find('br').remove();
    $('#cropDiv25').find('br').remove();
    $("#btnmfisin").attr('disabled',false);
    for(var i=0;i<document.getElementById('rowcount2').value;i++)
    {
        document.getElementById('cropDiv22').removeChild(document.getElementById('mfisin'+i));
        if(document.getElementById('mffolio'+i))
            document.getElementById('cropDiv23').removeChild(document.getElementById('mffolio'+i));
        if(document.getElementById('mfunits'+i))
            document.getElementById('cropDiv24').removeChild(document.getElementById('mfunits'+i));
        if(document.getElementById('mfaverageprice'+i))
            document.getElementById('cropDiv25').removeChild(document.getElementById('mfaverageprice'+i));
    }
    document.getElementById('rowcount2').value = "";

}

function inmutualE()
{
    // alert("inmutualE");
    // document.getElementById('edpid').value = "";
    // document.getElementById('eisin').value = "";
    // document.getElementById('eunits').value = "";
    // document.getElementById('eaverageprice').value = "";
    $('#cropDiv33').find('br').remove();
    $('#cropDiv34').find('br').remove();
    $('#cropDiv35').find('br').remove();
    $("#btneisin").attr('disabled',false);
    for(var i=0;i<document.getElementById('rowcount3').value;i++)
    {
        document.getElementById('cropDiv33').removeChild(document.getElementById('eisin'+i));
        if(document.getElementById('eunits'+i))
            document.getElementById('cropDiv34').removeChild(document.getElementById('eunits'+i));
        if(document.getElementById('eaverageprice' + i))
            document.getElementById('cropDiv35').removeChild(document.getElementById('eaverageprice' + i));

    }
    document.getElementById('rowcount3').value = "";

}