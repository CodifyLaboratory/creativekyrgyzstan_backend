
import React from "react";
import "./MainSlider.scss";
import MainSlider from "react-slick";
import CardForSlider from "./CardForSlider";

const CardSlider = ({slides}) => {

  const settings = {
    className: "center",  
    infinite:  false, 
    dots: false,
    autoplaySpeed: 2000,
    slidesToShow: 4,
    speed: 500,
    slidesToScroll: 4
  };
  const settingsMobile = {
    infinite:  false, 
    dots: false,
    autoplaySpeed: 2000,
    slidesToShow: 2,
    speed: 500,
    slidesToScroll : 2,
    rows:2,
    
  }
  return (
    <div className="main-slider">
      <div className="slider-line"/>
    <div className="tops-slider">
      <div className="WebVersion">
        
      <link
            rel="stylesheet"
            type="text/css"
            charset="UTF-8"
            href="https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.6.0/slick.min.css"
          />
          <link
            rel="stylesheet"
            type="text/css"
            href="https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.6.0/slick-theme.min.css"
          />

        <MainSlider {...settings}>
         
          {slides.map ((info,index) => (
               <CardForSlider key={index} img ={info.photo}
                name = {info.submit.full_name}
                company={info.submit.company_name}
                facebook={info.submit.facebook}
                inst={info.submit.instagram}
                telegram={info.submit.telegram}
                position={info.submit.position}/>
              ))}
          
        </MainSlider>
      
      </div>
      <div className="containerMobile">
        <MainSlider customPaging={(i)=><div className="dots-pag">{i+1}</div>} dotsClass="slick-dots"  {...settingsMobile}>
            {slides.map ((info,index) => (
               <CardForSlider key={index} img ={info.photo}
                name = {info.submit.full_name}
                company={info.submit.company_name}
                facebook={info.submit.facebook}
                inst={info.submit.instagram}
                telegram={info.submit.telegram}
                position={info.submit.position}/>
              ))}
        </MainSlider>
      </div>    
    </div>
    </div>
  );
};
export default CardSlider;
