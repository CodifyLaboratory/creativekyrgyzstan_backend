import React, { useEffect } from "react";
import Hero from "../section/Hero";
import Info from "../section/Info";
import Content from "../section/Content";
import CardItem from "../components/card/CardItem";
import CustomButton from "./button/CustomButton";
import '../sass/home.scss'
import { FormattedMessage } from 'react-intl'
function Home( { value } ) {
 

  useEffect(() =>{
    window.scrollTo(0, 0);
  },[])
  return (
    <div className="homePage-container">
      <Hero />
      <Info value={value} />
      <Content value={value} />
      <div className="MemberOfACI">
        <h2><FormattedMessage id="MembersOfACI"/></h2>
      </div>
      <CardItem />

      <div className="join_btn container">
      <a target="_blank" href="https://forms.gle/tmSP19PLXCeFdWcJ8" rel="noreferrer">
          <CustomButton
            type="outlined"
            className="join_btn"
          >
            <FormattedMessage id="Join"/>
          </CustomButton>
        </a>
      </div>
    </div>
  );
}

export default Home;
