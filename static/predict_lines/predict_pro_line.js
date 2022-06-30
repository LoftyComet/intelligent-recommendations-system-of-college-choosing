window.onload = function ()
{
    onSelectPro();
}

var linesInfo;
load_linesInfo();

function load_linesInfo()
{
	var url = "static/predict_lines/lines_info.json"
	var request = new XMLHttpRequest();
	request.open("get", url);
	request.send(null);
	request.onload = function () {
		if (request.status == 200) {/*返回状态为200，即为数据获取成功*/
            linesInfo=JSON.parse(request.responseText);
		}
	}
}

var pro_id_to_name= {"11": "北京", "12": "天津", "13": "河北", "14": "山西", "15": "内蒙古", "21": "辽宁", "22": "吉林", "23": "黑龙江", "31": "上海", "32": "江苏", "33": "浙江", "34": "安徽", "35": "福建", "36": "江西", "37": "山东", "41": "河南", "42": "湖北", "43": "湖南", "44": "广东", "45": "广西", "46": "海南", "50": "重庆", "51": "四川", "52": "贵州", "53": "云南", "54": "西藏", "61": "陕西", "62": "甘肃", "63": "青海", "64": "宁夏", "65": "新疆", "81": "香港", "82": "澳门"}
var subject_id_to_name={"1": "理科", "2": "文科", "3": "综合", "4": "艺术类", "5": "体育类", "23": "体育文", "24": "体育理", "25": "艺术文", "26": "艺术理", "31": "蒙授体育", "32": "蒙授文科", "33": "蒙授理科", "137": "汉授体育", "138": "汉授美术", "139": "蒙授美术", "140": "汉授音乐", "141": "蒙授音乐", "142": "汉授编导", "143": "其他艺术", "144": "蒙授其他艺术", "1079": "3+证书", "1084": "学考文", "1085": "学考理", "1144": "计算机类", "1145": "农学类", "1146": "牧医类", "1147": "烹饪类", "1148": "财会类", "1149": "美工设计类", "1150": "旅游类", "1151": "汽驾类", "1152": "建筑类", "1153": "机电类", "1154": "蒙牧医类", "1155": "化工类", "1156": "幼师类", "1157": "医学类", "1158": "采矿类", "1159": "畜牧兽医类", "1160": "农林类", "1938": "汉授其他艺术", "1988": "单独招生类", "2011": "美术类", "2013": "音乐类", "2073": "物理类", "2074": "历史类", "2279": "舞蹈类", "2280": "广播电视编导类", "2281": "书法类"}

var baseOption = {
    title:
    {
        text: 'baseOption'
    },
    tooltip:
    {
//        trigger: 'axis',
//        axisPointer: {
//          type: 'cross',
//          label: {
//            backgroundColor: '#6a7985'
//          }
//        }
    },
    legend: // 图例
    {
        data: [ '一本线', '二本线','三本线']
    },
    grid:
    {
        left: '3%',
        right: '3%',
        bottom: '3%',
        containLabel: true
    },
//  toolbox: {
//    feature: {
//      saveAsImage: {}
//    }
//  },
    xAxis:
    {
        type: 'category',
        boundaryGap: false,
        data: ['2018', '2019', '2020', '2021', '2022(预测)']
    },
    yAxis:
    {
        type: 'value'
    },
    series:
    [
        {
            name: '一本线',
            type: 'line',
            // stack: 'Total',
            data: [150, 232, 201, 154, 190]
        },
        {
            name: '二本线',
            type: 'line',
            // stack: 'Total',
            data: [220, 182, 191, 234, 290]
        },
        {
            name: '三本线',
            type: 'line',
            // stack: 'Total',
            data: [120, 132, null,101,  90]
        },
    ]
};

function onSelectPro()
{
    // window.alert("onSelectPro");
	// 获取 选择的省份id
    let proId = document.getElementById("select_pro").value;

	var selectType = document.getElementById("select_type");
	selectType.options.length = 0;
	let types=linesInfo[proId];
	for(var key in types){
		selectType.options.add(new Option( subject_id_to_name[key],key));
    }
    refreshChart();
}

function onSelectType()
{
    refreshChart();
}

function refreshChart()
{
	// 根据选中的省份和类别统计信息
    let proId = document.getElementById("select_pro").value;
    let typeId=document.getElementById("select_type").value;
//    console.log(typeId);
    let option=JSON.parse(JSON.stringify(baseOption));
    // console.log(linesInfo[proId]);
    let lines=linesInfo[proId][typeId];
//    console.log(lines);
    let legend=[]
    let years=[]
    let datas={}
    for(let item of lines)
    {
        let year=item['year'];
        let batch_name=item['batch_name'];
        if(legend.indexOf(batch_name)==-1)
        {
            legend.push(batch_name);
        }
        if(years.indexOf(year)==-1)
        {
            years.push(year);
        }
    }
    // console.log("year "+years);
    for(let l of legend)
    {
        datas[l]={};
        for(let x of years)
        {
            datas[l][x]=null;
        }
    }
    for(let item of lines)
    {
        let year=item['year'];
        let batch_name=item['batch_name'];
        let score=item['score'];
//        console.log(year,batch_name,score);
        if(! (batch_name in datas))
        {
            // window.alert("new {}");
            datas[batch_name]={};
        }
        datas[batch_name][year]=score;
    }

    let series=[];
    for(let l of legend) // 图例
    {
        let d=[];
        for(let y of years)
        {
            d.push(datas[l][y]);
        }
        series.push({
            name: l,
            type: 'line',
            label: {show: true},
            data: d
        });
    }

	// 统计结束，开始画表
	var myChart = echarts.init(document.getElementById('main'));

	option.title.text=pro_id_to_name[proId];

    option.legend.data=legend;

    let pos2022=years.indexOf('2022');
    if(pos2022!=-1)
        years[pos2022]="2022(预测)"
    // console.log(years);
    option.xAxis.data=years;

    option.series=series;

	myChart.setOption(option);
}
